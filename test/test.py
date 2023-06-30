from pytube import YouTube


yt = YouTube("https://www.youtube.com/watch?v=k1gf2TOYMls")
try:
    yt.streams.filter(only_audio=True).first()
except:
    print("fail download mp3")

print(yt)
