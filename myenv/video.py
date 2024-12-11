from pytube import YouTube

video_url = "https://youtu.be/NJLD9hw6inw"
yt = YouTube(video_url)

audio_streams = yt.streams.filter(only_audio=True)
if audio_streams:
    audio_stream = audio_streams.first()
    name = f'{yt.title}.mp3'
    audio_stream.download(filename=name)
else:
    print("Аудиопоток не найден")