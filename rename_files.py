"""
rename_files.py
    Capabilities:
        Will start the count on whatever files is in the index 0
    Limitations:
        If the user will run this program twice, the renamed file might be renamed different from previous
    Improvements:

    Prerequisite:
        
"""
import os  # for the rename function

# Rename the files
def rename_files(directory, new_name):
    files = os.listdir(directory)  # Path of the file
    counter = 0  # For reiterating files
    for file in files:
        # Extract the file type and keep the file format (Ex. .txt)
            file_type = file.split('.')[-1]
        # Get a path and turn it into another path
            os.rename(f'{directory}/{file}', f'{directory}/{new_name}_{str(counter)}.{file_type}')
            print(f'Renaming {file} to {new_name}_{str(counter)}.{file_type}' )
            # Increment the file counter
            counter += 1

# Call the rename_files function
rename_files('/home/renzo/Documents/rename_prac_folder', 'my_new_name')

print('\nRenaming files successful!\n')