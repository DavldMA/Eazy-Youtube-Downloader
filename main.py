import zipfile
import os
import time
import downloadHandler as dh
import fetchPlaylist as fp
from colorama import Fore, Style
from tqdm import tqdm

def zipFiles(filePaths, zipPath):
    try:
        with zipfile.ZipFile(zipPath, 'w') as zipf:
            for filePath in filePaths:
                zipf.write(filePath, arcname=os.path.basename(filePath))
        print("Files zipped successfully on " + zipPath + "!")
    except Exception as e:
        print("Error:", e)

def deleteFiles(filePaths):
    for filePath in filePaths:
        try:
            os.remove(filePath)
        except Exception as e:
            print(f"Error deleting: {filePath}, {e}")

def main():
    playlistLink = input(Fore.GREEN + "Enter playlist link: " + Style.RESET_ALL)
    maxResults = int(input(Fore.GREEN + "Enter number of results you want, type 0 if u want the whole playlist: " + Style.RESET_ALL))
    downloadType = input(Fore.GREEN + "Download as video[v], as audio[a]" + Style.RESET_ALL)
    video_urls_iterator = iter(fp.getVideosFromPlaylist(playlistLink, maxResults))

    savePath = "downloaded/"
    zipFileName = "download"+ str(round(time.time() * 1000)) + ".zip"
    zipFilePath = os.path.join(savePath, zipFileName)

    with tqdm(desc="Fetching URLs", unit="video") as pbar:
        urls = []
        while True:
            try:
                video_url = next(video_urls_iterator)
                if video_url:
                    urls.append(video_url)
                    pbar.update(1) 
            except StopIteration:
                break

    with tqdm(total=len(urls), desc="Downloading", unit="file") as pbar:
        downloadPath = []
        for url in urls:
            if(downloadType.lower() == "a"):
                audioPath = dh.downloadAudio(url, savePath)
                if audioPath:
                    downloadPath.append(audioPath)
            elif(downloadType.lower() == "v"):
                videoPath = dh.downloadVideo(url, savePath)
                if videoPath:
                    downloadPath.append(videoPath)
            else:
                print(Fore.RED + "This is not a valid option..." + Style.RESET_ALL)
                break
            pbar.update(1)
    zipFiles(downloadPath, zipFilePath)
    deleteFiles(downloadPath)
    
main()