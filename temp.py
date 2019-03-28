#%%


# def extractTag(stream):
#     # itag mime_type res fps vcodec acodec
#     temp = stream
#     data = {'itag':None, 'mime_type':None, 'res':None, 'fps':None,\
#         'vcodec':None, 'acodec':None, 'abr':None}
#     data['itag'] = temp.itag
#     data['mime_type'] = temp.mime_type
#     if temp.includes_video_track:
#         data['res'] = temp.resolution
#         data['fps'] = temp.fps
#         if not temp.is_adaptive:
#             data['vcodec'] = temp.video_codec
#             data['acodec'] = temp.audio_codec
#         else:
#             data['vcodec'] = temp.video_codec
#     else:
#         data['abr'] = temp.abr
# #         data['acodec'] = temp.audio_codec

# #     return data


from pytube import YouTube, extract


link = 'https://www.youtube.com/watch?v=C8ywSPOsB1o'

yt = YouTube(link)
tmep = yt.streams.filter(only_video=True).all()

# print(yt.streams.filter(only_video=True).first())
# stream = temp.order_by('abr')
# stream.download()
# tempData = list()

# for stream in allStream:
#     tempData.append(extractTag(stream))

# tempData


# import os

# # allStream = yt.streams.all()
# ffmpeg_path = '.\\ffmpeg\\bin\\ffmpeg.exe'
# os.system('{ffmpeg_path} -i video.mp4 -i audio.mp3 -c:v copy -c:a ac3 -b:a 320K output.mp4'.format(ffmpeg_path=ffmpeg_path))