import youtube_dl

download_options = {"format" : "bestaudio/best",
                     "postprocessors" : [{
                         "key": "FFmpegExtractAudio",
                         "preferredcodec" : "mp3",
                         "preferredquality" : "192",}], }

youtube_link = input("Enter youtube link: ")


with youtube_dl.YoutubeDL(download_options) as ydl:
    ydl.download([youtube_link])
 
