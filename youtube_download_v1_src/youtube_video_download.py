"""
youtube_video_download.py
    Capabilities:
        Can download videos with more than 1 hour playing time 
        Download youtube videos
        Download youtube and convert into mp4
        Save downloaded file to specified folder
    Limitations:
        Can't download in bulk.
        If the file is already downloaded, it will just overwrite the previous
            downloaded file.
    Prerequisites:
        Install pytube library
    Improvement:
        Add download progress, might need moviepy

"""

from pytube import YouTube
from sys import argv  # Used interact closely with the interpreter

# argv[0] is the module name: youtube_downloader.py
# argv[1] is the link: $ python3 youtube_download_v1_src/youtube_video_download.py 'https://www.youtube.com/watch?v=sE1qn8mmNF8'
link = argv[1]  # executes the first command line argument
yt = YouTube(link)

print(f'Title: {yt.title}')
num_views = yt.views
print(f'Views: {num_views:,}')

print('\nDownload in progress. Please wait...\n')

# Download the youtube video .mp4 (highest resolution)
youtube_dl = yt.streams.get_highest_resolution()
youtube_dl.download('/home/renzo/Videos/youtube_downloads')  # Download path

print('\nDownload successful.\n')




