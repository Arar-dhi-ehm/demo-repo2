"""
youtube_downloader.py
    Capabilities:
        Can download videos or music with more than 1 hour playing time 
        Download youtube videos one at a time
        Download youtube sound only but still mp4 format
        Download youtube and convert into mp4
        Save downloaded file to specified folder
    Prerequisites:
        Install pytube library
"""

from pytube import YouTube
from sys import argv  # what is this for? To interact closely with the interpreter
import pyautogui as pag

# argv[0] is the module name: youtube_downloader.py
# argv[1] is the link: $ python3 youtube_downloader.py 'https://www.youtube.com/watch?v=vEQ8CXFWLZU'
link = argv[1]  # executes the first command line argument
yt = YouTube(link)

# Test if it will work
print('Title: ', yt.title)
num_views = yt.views
print(f'Views: {num_views:,}')

print('\nDownload in progress. Please wait...\n')

# Download the youtube video .mp4 (highest resolution)
youtube_dl = yt.streams.get_highest_resolution()
youtube_dl.download('/home/renzo/Videos/youtube_downloads')  # Download path

# Download youtube mp3
# youtube_dl = yt.streams.get_audio_only()
# youtube_dl.download('/home/renzo/Videos/youtube_downloads')  # Download path

# Alert when finished
pag.alert(text='Download Finished.', title='DONE!', button='OK')




