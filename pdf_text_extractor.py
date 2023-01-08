"""
pdf_text_extractor.py
    Capabilities:
        Convert pdf to text
    Limitations:
        No idea yet if how many pages it can extract
        It might not be always accurate if there are image or tables and etc.
    Improvements:
        Add a button to copy the converted text
    Prerequisite:
        Install pypdf2 package
"""
import PyPDF2
import tkinter
from tkinter import filedialog

# This is the window widget (container)
window = tkinter.Tk()
window.title('PDF Text Extractor')


def open_file():
    # This will store the name of the file that will be opened
    filename = filedialog.askopenfilename(
        title='Open PDF File',
        # Will open a file dialogue in this directory
        initialdir='/home/renzo/Documents/automation_scripts/automation_project/extract_pdf_text',
        # It will show any(*) files that ends with .pdf
        filetypes=[('PDF files', '*.pdf')])
    print(filename)

    # Reader Object
    reader = PyPDF2.PdfReader(filename)
    # Extract text from pdf using for loop and show it in the terminal
    for page_number in range(len(reader.pages)):
        current_text = reader.pages[page_number].extract_text()
        print(current_text)


file_name_label = tkinter.Label(window, text='No file selected')
output_file_text = tkinter.Text(window)
open_file_text = tkinter.Button(window, text='Open PDF File', command=open_file)

# To show in the popup
file_name_label.pack()
output_file_text.pack()
open_file_text.pack()

# This will create an infinite loop of the app
window.mainloop()