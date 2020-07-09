from pytube import YouTube

yt = YouTube('https://youtu.be/9bZkp7q19f0')
print(yt.title)
stream = yt.streams.first()
stream.download()

'''
# yt = YouTube('https://youtu.be/9bZkp7q19f0')
# YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()
YouTube("http://youtube.com/watch?v=9bZkp7q19f0").streams.first()
'''

'''
(yt.streams
.filter(progressive=True, file_extension='mp4')
.order_by('resolution')[-1]
.download())

print(yt.streams)
'''


'''
YouTube('https://www.youtube.com/results?search_query=%E8%BD%89%E7%9C%BC')
# yt = YouTube('https://www.youtube.com/results?search_query=%E8%BD%89%E7%9C%BC')
print(yt.streams)
# yt.streams.filter(progressive=True)
'''
