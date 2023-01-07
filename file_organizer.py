#! python3
"""
file_organizer.py

    Capabilities:
		It moves and sort files with specified format and move it into a designated folder
		It can be run again to reorganize your files
    Limitations:
		It can only move files not directories/folders
		Modify condition if necessary

"""
import pyautogui as pag
import os
import shutil

# The path means directory of the folder where you want things to be organized.
path = "/home/renzo/Documents/automation_scripts/organize_files_here/"
names = os.listdir(path)

# The files will be organized into different folders specified by the folder_name
folder_name = ['CSV','XLSX','DOCX','PPTX','PDFs','Installers','TORRENTS','PNG','JPG','TXT','ZIP','RAR','MP3','MP4','MSI','ISO']
for x in range(0, 16):
	if not os.path.exists(path + folder_name[x]):
		os.makedirs(path + folder_name[x])

for files in names:
	if ".csv" in files and not os.path.exists(path + 'CSV/' + files):
		shutil.move(path + files, path + 'CSV/' + files)
  
	if ".xlsx" in files and not os.path.exists(path + 'XLSX/' + files):
		shutil.move(path + files, path + 'XLSX/' + files)
  
	if ".docx" in files and not os.path.exists(path + 'DOCX/' + files):
		shutil.move(path + files, path + 'DOCX/' + files)
  
	if ".pptx" in files and not os.path.exists(path + 'PPTX/' + files):
		shutil.move(path + files, path + 'PPTX/' + files)
  
	if ".pdf" in files and not os.path.exists(path + 'PDFs/' + files):
		shutil.move(path + files, path + 'PDFs/' + files)
  
	if ".exe" in files and not os.path.exists(path + 'Installers/' + files):
		shutil.move(path + files, path + 'Installers/' + files)
  
	if ".torrent" in files and not os.path.exists(path + 'TORRENTS/' + files):
		shutil.move(path + files, path + 'TORRENTS/' + files)
  
	if ".png" in files and not os.path.exists(path + 'PNG/' + files):
		shutil.move(path + files, path + 'PNG/' + files)
  
	if ".jpg" in files and not os.path.exists(path + 'JPG/' + files):
		shutil.move(path + files, path + 'JPG/' + files)
  
	if ".txt" in files and not os.path.exists(path + 'TXT/' + files):
		shutil.move(path + files, path + 'TXT/' + files)
  
	if ".zip" in files and not os.path.exists(path + 'ZIP/' + files):
		shutil.move(path + files, path + 'ZIP/' + files)
  
	if ".rar" in files and not os.path.exists(path + 'RAR/' + files):
		shutil.move(path + files, path + 'RAR/' + files)
  
	if ".mp3" in files and not os.path.exists(path + 'MP3/' + files):
		shutil.move(path + files, path + 'MP3/' + files)
  
	if ".mp4" in files and not os.path.exists(path + 'MP4/' + files):
		shutil.move(path + files, path + 'MP4/' + files)
  
	if ".msi" in files and not os.path.exists(path + 'MSI/' + files):
		shutil.move(path + files, path + 'MSI/' + files)
  
	if ".iso" in files and not os.path.exists(path + 'ISO/' + files):
		shutil.move(path + files, path + 'ISO/' + files)

# Script is finished
pag.alert(text='Script is finished.', title='DONE!', button='OK')