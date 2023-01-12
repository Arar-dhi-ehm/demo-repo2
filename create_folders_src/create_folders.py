"""
create_folders.py
    Capabilities:
        Create multiple folders from excel file data
    Limitations:
        Can't create a line for subfolders
        Can't determine which folder is a duplicate
        Will not overwrite a duplicate folder
    Improvements:

    Note:
        Spreadsheet with 2 columns of data
        
"""

import os  # For creating folder 
import openpyxl  # For reading excel files

result_location = '/home/renzo/Documents/python_prac'
spreadsheet_data = '/home/renzo/Documents/git/test_1.xlsx'

# Load the spreadsheet file
workbook = openpyxl.load_workbook(spreadsheet_data)
# Define sheet to use
sheet = workbook['Sheet1']

column_values = [cell.value for col in sheet.iter_cols(
                min_row=2, max_row=None, min_col=2, max_col=2) 
                for cell in col]

# Create loop to go through the values 1 by 1
for value in column_values:
    print(f'Creating folder: {value}')
print('\nPlease wait...\n')

# Create Folders
try:
    for value in column_values:
        folder_name = value
        base_directory = result_location
        os.makedirs(os.path.join(base_directory, folder_name))  # Join directory and folder name
        print(f'Folder created: {folder_name}')
    print('\nDone!\n')
except FileExistsError:
    print('Error: A folder with the same name already exist.')