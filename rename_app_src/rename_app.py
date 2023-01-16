"""
rename_app.py
    Capabilities:
        Rename files in bulk
        Add and remove specified prefix
        Add and remove specified suffix
        Use new name for files
    Limitations:
        
    Improvements:

    Prerequisite:
        Install pyqt5 package
        Create GUI using Qt Designer app
"""
import os  # For the rename function
import re  # For filtering a certain pattern (Regex)

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *  # Don't use wildcard imports for real projects. For Demo only
from PyQt5 import uic

class MyGUI(QMainWindow):
    # Load the UI
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('rename_app_src/bulk_gui.ui', self)
        self.show()

        # Define default values
        self.directory = '.'
        self.list_model = QStandardItemModel()
        self.select_model = QStandardItemModel()

        self.select_view.setModel(self.select_model)
        # Keep track of selections
        self.selected = []

        # Connect options and buttons to its functions
        self.action_open_directory.triggered.connect(self.load_directory)
        self.filter_button.clicked.connect(self.filter_list)
        self.select_button.clicked.connect(self.choose_selection)
        self.remove_button.clicked.connect(self.remove_selection)
        self.apply_button.clicked.connect(self.rename_files)

    def load_directory(self):
        self.directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        # Look for every file in the directory
        for file in os.listdir(self.directory):
            # Will only get the files in the directory not subdirectory
            if os.path.isfile(os.path.join(self.directory, file)):
                # Add to the list_model
                self.list_model.appendRow(QStandardItem(file))
        self.list_view.setModel(self.list_model)

    def rename_files(self):
        counter = 1
        for file_name in self.selected:
            if self.add_prefix.isChecked():
                # Rename the file
                os.rename(os.path.join(self.directory, file_name),
                          os.path.join(self.directory, self.name_edit.text() + file_name))
            elif self.remove_prefix.isChecked():
                # Check if the file_name actually starts with the prefix
                if file_name.startswith(self.name_edit.text()):
                    # Rename the current file name using index slicing
                    os.rename(os.path.join(self.directory, file_name),
                              os.path.join(self.directory, file_name[len(self.name_edit.text()):]))
            elif self.add_suffix.isChecked():
                file_type = file_name.split('.')[-1]
                os.rename(os.path.join(self.directory, file_name),
                          os.path.join(self.directory, file_name[:-(len(file_type) + 1)] + self.name_edit.text() 
                          + '.' + file_type))
            elif self.remove_suffix.isChecked():
                file_type = file_name.split('.')[-1]
                if file_name.endswith(self.name_edit.text() + '.' + file_type):
                    os.rename(os.path.join(self.directory, file_name),
                              os.path.join(self.directory, file_name[:-len(self.name_edit.text() + '.' + file_type)]
                                           + '.' + file_type))
            elif self.new_name.isChecked():
                file_type = file_name.split('.')[-1]
                os.rename(os.path.join(self.directory, file_name),
                          os.path.join(self.directory, self.name_edit.text() + str(counter) + '.' + file_type))
                counter += 1
            else:
                print('Select a radio button')

            self.selected = []
            self.select_model.clear()
            self.list_model.clear()

            for file in os.listdir(self.directory):
                if os.path.isfile(os.path.join(self.directory, file)):
                    self.list_model.appendRow(QStandardItem(file))
            self.list_view.setModel(self.list_model)

    def choose_selection(self):
        if len(self.list_view.selectedIndexes()) != 0:
            # If not 0, move to selected view
            for index in self.list_view.selectedIndexes():
                if index.data() not in self.selected:
                    self.selected.append(index.data())
                    self.select_model.appendRow(QStandardItem(index.data()))

    def remove_selection(self):
        try:
            if len(self.select_view.selectedIndexes()) != 0:
                for index in reversed(sorted(self.select_view.selectedIndexes())):
                    # Remove elements from index data
                    self.selected.remove(index.data())
                    self.select_model.removeRow(index.row())
        # If there's an error it will print it.
        except Exception as e:
            print(e)

    def filter_list(self):
        # Everything that is selected is going to be cleared
        self.select_model.clear()
        self.selected = []
        # Get individual items from individual indices
        for index in range(self.list_model.rowCount()):
            item = self.list_model.item(index)
            # If the pattern matched
            if re.match(self.filter_edit.text(), item.text()):
                self.select_model.appendRow(QStandardItem(item.text()))
                self.selected.append(item.text())


app = QApplication([])
window = MyGUI()
app.exec_()