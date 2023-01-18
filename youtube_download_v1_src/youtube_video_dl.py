from pytube import YouTube

# URL input from user
yt = YouTube(str(input('\nEnter the URL of the video you want to download: \n>> ')))

print('\nDownload in progress, please wait...\n')
video = yt.streams.get_highest_resolution()

# Ask for saved file destination
print('Enter the destination (if current directory, leave it blank)')
destination = str(input('>> '))

# File download
video_file = video.download(output_path=destination)

print(f'\nTitle: {yt.title}')
print(f'Views: {yt.views:,}')
print(f'Author: {yt.author}')
print(f'Publish Date: {yt.publish_date}')

print('\nDownload successful.\n')