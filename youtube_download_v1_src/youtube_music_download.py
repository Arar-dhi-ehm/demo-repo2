"""
youtube_music_download.py
    Capabilities:
        Can download music with more than 1 hour playing time 
        Download youtube audio
        Save downloaded file to specified folder
    Limitations:
        Can't download in bulk.
        If the file is already downloaded, it will just overwrite the previous
            downloaded file.
    Prerequisites:
        Install pytube and moviepy library
    Improvement:
        Add download progress, might need moviepy

"""
import os
from pytube import YouTube
from sys import argv  # what is this for? To interact closely with the interpreter

# argv[0] is the module name: youtube_music_download.py
# argv[1] is the link: $ python3 youtube_download_v1_src/youtube_music_download.py 'https://www.youtube.com/watch?v=sE1qn8mmNF8'
link = argv[1]  # executes the first command line argument
yt = YouTube(link)
download_path = '/home/renzo/Videos/youtube_downloads'

print('Title: ', yt.title)
num_views = yt.views
print(f'Views: {num_views:,}')

print('\nDownload in progress. Please wait...\n')

# Download youtube mp4 but audio only
youtube_dl = yt.streams.get_audio_only()
youtube_dl.audio.write_audiofile(youtube_dl[:-4] + ".mp3")
youtube_dl.close()
music_dl = youtube_dl.download(download_path)  # Download path
os.rename(f'{download_path}/{music_dl[:-1]}', f'{download_path}/{music_dl[:-1] + 3}')

# Download youtube mp3 [working]
# youtube_dl = yt.streams.get_audio_only()
# youtube_dl.download(download_path)  # Download path

print('\nDownload successful.\n')




