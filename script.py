import sys
from pytube import YouTube

def check_choose():
	try:
		choose = int(input(": "))
		if (choose > 0) and (choose <= len(streams_resolutions)):
			return choose
		else:
			print("Invalid choice")
			sys.exit
	except ValueError:
		print("Invalid resolution")
		sys.exit

print("Enter the url")
url = input(": ")
print("Checking your url, take a cofe break😜...")
youtube_video = YouTube(url)

streams = youtube_video.streams.filter(progressive=True)
streams_itags = []
streams_resolutions = []

# Récupération des tags et des résolutions
for stream in streams:
	streams_itags.append(stream.itag)
	streams_resolutions.append(stream.resolution)

i = 0
print("Choose a resolution")
for tag in range(0, len(streams_itags)):
	print(str(i+1) + ". " + streams_resolutions[i])
	i += 1

choosed_resolution = int(check_choose()) - 1
choosed_stream = streams.get_by_itag(streams_itags[choosed_resolution])
print("Downloading your video, take another cofe break🙃...")
choosed_stream.download()
print("Download finished😋")