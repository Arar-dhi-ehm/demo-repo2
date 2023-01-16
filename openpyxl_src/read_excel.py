"""
read_excel.py
    Capabilities:

    Limitations:

    Prerequisite:
        pip install openpyxl
"""

import openpyxl

workbook = openpyxl.load_workbook('/home/renzo/Documents/git/excel_sample.xlsx')

# Print the name of the sheets in excel file
# sheets = workbook.sheetnames
# print(sheets)

# Print the active title(tab_name) in the excel
# print(workbook.active.title)

sheet_1 = workbook['Info']
# Store the value of any cell inside Info tab
value = sheet_1['C4'].value
# print(f'Name: {value}')

# Method 1
print(workbook['Info']['A3'].value)



