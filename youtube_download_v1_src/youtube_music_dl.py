from pytube import YouTube
import os

# URL input from user
yt = YouTube(str(input('\nEnter the URL of the video you want to download: \n>> ')))

print('\nDownload in progress, please wait...\n')

# Extract audio only
video = yt.streams.filter(only_audio=True).first()

# Ask for saved file destination
print('Enter the destination (if current directory, leave it blank)')
destination = str(input('>> '))

# File download
music_file = video.download(output_path=destination)

# Save the file and change format to .mp3
base_name, file_format = os.path.splitext(music_file)
new_file = base_name + '.mp3'
os.rename(music_file, new_file)

print(f'\nTitle: {yt.title}')
print(f'Views: {yt.views:,}')
print(f'Author: {yt.author}')
print(f'Publish Date: {yt.publish_date}')

print('\nDownload successful.\n')
