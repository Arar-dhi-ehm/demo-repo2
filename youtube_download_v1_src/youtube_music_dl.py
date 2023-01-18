from pytube import YouTube
import os

# URL input from user
yt = YouTube(str(input('\nEnter the URL of the video you want to download: \n>> ')))

# Extract audio only
video = yt.streams.filter(only_audio=True).first()

print('\nDownload in progress, please wait...\n')

# Ask for saved file destination
print('\nEnter the destination (if current directory, leave it blank)')
destination = str(input('>> ')) or '.'

# File download
music_file = video.download(output_path=destination)

# Save the file
base_name, file_format = os.path.splitext(music_file)
new_file = base_name + '.mp3'
os.rename(music_file, new_file)

print(f'\nTitle: {yt.title}')

# num_views = yt.views
# print(f'Views: {num_views:,}')

print(f'Views: {yt.views:,}')

print(f'Author: {yt.author}')

print(f'Publish Date: {yt.publish_date}')

print('\nDownload successful.\n')
