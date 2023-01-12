"""
rename_files.py
    Capabilities:
        Will start the count on whatever files is in the index 0
        Filter by ending
    Limitations:
        If the user will run this program twice, the renamed file might be renamed different from previous
        No exception for files only filter
    Improvements:

    Prerequisite:
        
"""
import os  # for the rename function

# Rename the files
def rename_files(directory, ending, new_name):
    files = os.listdir(directory)  # Path of the file
    counter = 0  # For reiterating files
    for file in files:
            # Filter by ending or file format
            if file.endswith(ending):
            # Extract the file type and keep the file format (Ex. .txt)
                file_type = file.split('.')[-1]
            # Get a path and turn it into another path
                os.rename(f'{directory}/{file}', f'{directory}/{new_name}_{str(counter)}.{file_type}')
                print(f'Renaming {file} to {new_name}_{str(counter)}.{file_type}' )
                # Increment the file counter
                counter += 1

"""File Types for Filter:
Document - docx, pdf, txt, pptx, ppt, ods, odt,
Spreadsheet - xlsx, xls, 
Image - png, jpg, jpeg
Other - rar, deb, zip, 7z

"""
# Call the rename_files function but only rename files ending with this format. ending='file_type'
rename_files('/home/renzo/Documents/rename_prac_folder','pdf' ,'my_new_name')

print('\nRenaming files successful!\n')