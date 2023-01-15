
import os
import sys
import platform
import subprocess

# Seeing if the file exists
if os.path.exists(sys.argv[1]):
    file = open(sys.argv[1], "r")
    file_contents = file.read()
    file.close()
else:
    print("Usage: copytoclipboard <file_name>")
    exit(1)

whatos = platform.system()

try:
    if whatos == "Linux":
        subprocess.run("xclip", universal_newlines=True, input=file_contents) # copy to clipboard not yet working
        print("success: copied to clipboard")
    elif whatos == "Windows":
        subprocess.run("clip", universal_newlines=True, input=file_contents)
        print("success: copied to clipboard")
    elif whatos == "Windows":
        subprocess.run("pbcopy", universal_newlines=True, input=file_contents)
        print("success: copied to clipboard")
    # else:
    #     print("failed: clipboard not supported")
except Exception as e:
    print(e)