import os
import re
from pytube import YouTube


def generateSafeFilename(title):
    # Replace invalid characters with underscores
    return re.sub(r'[\\/*?:"<>|]', '_', title)

def downloadAudio(urls, savePath):
    print("---------------")
    print(f"Title: {urls['title']}")
    print(f"Video ID: {urls['video_id']}")
    url = "https://www.youtube.com/watch?v=" + urls['video_id']
    
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        if stream:
            audioTitle = generateSafeFilename(yt.title)
            audioPath = os.path.join(savePath, audioTitle + '.mp4')
            stream.download(output_path=savePath)
            os.rename(os.path.join(savePath, stream.default_filename), audioPath)
            print("Audio download successful!")
            return audioPath
        else:
            print("No suitable audio stream found.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

def downloadVideo(urls, savePath):
    print("---------------")
    print(f"Title: {urls['title']}")
    print(f"Video ID: {urls['video_id']}")
    url = "https://www.youtube.com/watch?v=" + urls['video_id']
    
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if stream:
            videoTitle = generateSafeFilename(yt.title)
            videoPath = os.path.join(savePath, videoTitle + '.mp4')
            stream.download(output_path=savePath)
            # Rename the downloaded file to the sanitized title
            os.rename(os.path.join(savePath, stream.default_filename), videoPath)
            print("Video download successful!")
            return videoPath
        else:
            print("No suitable video stream found.")
            return None
    except Exception as e:
        print("Error:", e)
        return None
