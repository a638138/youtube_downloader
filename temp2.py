import pafy

url = "https://www.youtube.com/watch?v=Z1IZYjUGxFk"
video = pafy.new(url)

print(video)

# videodata = video.getbestaudio()
audiodata = video.getbestaudio()

# videodata.download()
audiodata.download()