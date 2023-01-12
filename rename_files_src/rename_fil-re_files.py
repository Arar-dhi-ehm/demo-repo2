"""
rename_files.py
    Capabilities:
        Will start the count on whatever files is in the index 0
        Filter files that contains this pattern, then rename
    Limitations:
        If the user will run this program twice, the renamed file might be renamed different from previous
        No exception for files only filter
    Improvements:

    Prerequisite:
        
"""
import os  # For the rename function
import re  # For filtering a certain pattern (Regex)

# Rename the files
def rename_files(directory, pattern, new_name):
    files = os.listdir(directory)  # Path of the file
    counter = 0  # For reiterating files
    for file in files:
            # Filter by pattern
            if re.match(pattern, file):
            # Extract the file type and keep the file format (Ex. .txt)
                file_type = file.split('.')[-1]
            # Get a path and turn it into another path
                os.rename(f'{directory}/{file}', f'{directory}/{new_name}_{str(counter)}.{file_type}')
                print(f'Renaming {file} to {new_name}_{str(counter)}.{file_type}' )
                # Increment the file counter
                counter += 1

# Filter 1: Call the rename_files function but only rename files with the specified pattern. 
# Dot '.' means any letter. Star Expression '*' means unpack everything
# rename_files('/home/renzo/Documents/rename_prac_folder', 'my.*', 'success')

# Filter 2: Rename files that has a number in its filename
# Whatever '.', how many times you want '*', has [0-9] number at the end
rename_files('/home/renzo/Documents/rename_prac_folder', '.*[0-9].*', 'number')

print('\nRenaming files successful!\n')