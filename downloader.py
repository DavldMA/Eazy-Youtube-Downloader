from pytube import Playlist, YouTube
from colorama import Fore, Style
from unidecode import unidecode
from tqdm import tqdm
import zipfile
import shutil
import os
import re

currentDirectory = os.getcwd()

def download(url, isAudio=False):
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        if isYoutubePlaylistLink(url):
            downloadPlaylist(url, isAudio)
        else:
            downloadSingle(url, isAudio)

        if isAudio:
            zipFiles(currentDirectory + "/temp/audioTemp/", currentDirectory + "/download/audios.zip")
        else:
            zipFiles(currentDirectory + "/temp/videoTemp/", currentDirectory + "/download/videos.zip")
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

def downloadPlaylist(url, isAudio=False):
    playlist = Playlist(url)
    print(f'{Fore.GREEN}[+] Playlist Title: {playlist.title}{Style.RESET_ALL}')
    print(f'{Fore.GREEN}[+] Number of Videos on the Playlist: {len(playlist.video_urls)}{Style.RESET_ALL}')
    for videoURL in playlist:
        downloadSingle(videoURL, isAudio)

def downloadSingle(url, isAudio=False):
    youtube = YouTube(url)
    printUrlInfo(youtube)
    if isAudio:
        youtubeDonwloader = youtube.streams.get_audio_only()
        downloadWithProgress(youtubeDonwloader, currentDirectory + "/temp/audioTemp/", generateSafeFilename(youtube.title) + ".mp4")
    else:
        youtubeDonwloader = youtube.streams.get_highest_resolution()
        downloadWithProgress(youtubeDonwloader, currentDirectory + "/temp/videoTemp/", generateSafeFilename(youtube.title) + ".mp4")
    os.system('cls' if os.name == 'nt' else 'clear')

def downloadWithProgress(stream, destination, filename):
    file_path = os.path.join(destination, filename)
    with tqdm(total=stream.filesize, desc=f"[+] Downloading {filename}", unit="B", unit_scale=True) as progress_bar:
        stream.download(destination)
        progress_bar.update(stream.filesize - progress_bar.n)

def isYoutubeVideoLink(url):
    youtubeVideoPatterns = [
        r"(https?://)?(www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})",
        r"(https?://)?(www\.)?youtu\.be/([a-zA-Z0-9_-]{11})"
    ]

    for pattern in youtubeVideoPatterns:
        if re.match(pattern, url):
            return True

    return False

def isYoutubePlaylistLink(url):
    youtubePlaylistPatterns = [
        r"(https?://)?(www\.)?youtube\.com/playlist\?list=([a-zA-Z0-9_-]+)",
        r"(https?://)?(www\.)?youtu\.be/([a-zA-Z0-9_-]+)"
    ]

    for pattern in youtubePlaylistPatterns:
        if re.match(pattern, url):
            return True

    return False

def printUrlInfo(url):
    print(f"{Fore.GREEN}[+] Downloading: {url.title}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] Views: {url.views} | Duration: {secondsToHms(url.length)}{Style.RESET_ALL}")

def getLink():
    while True:
        url = input(f"{Fore.YELLOW}[+] Paste the link of the video here: {Style.RESET_ALL}")
        if isYoutubeVideoLink(url) or isYoutubePlaylistLink(url):
            return url
        print(f"{Fore.RED}[-] This is not a youtube video link nor a youtube playlist. Press enter to continue{Style.RESET_ALL}")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

def zipFiles(filePaths, zipPath):
    try:
        unique_zip_path = createUniqueZipName(os.path.dirname(zipPath), os.path.basename(zipPath).split('.')[0], 'zip')
        with zipfile.ZipFile(unique_zip_path, 'w') as zipf:
            for root, _, files in os.walk(filePaths):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, filePaths)
                    zipf.write(file_path, arcname=arcname)

        print(f"{Fore.GREEN}[+] Folder zipped successfully to {unique_zip_path}{Style.RESET_ALL}")

        # Delete the temporary folder after zipping
        shutil.rmtree(filePaths)
        print(f"{Fore.GREEN}[+] Temporary folder '{filePaths}' deleted.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

def createUniqueZipName(base_path, base_name, extension):
    count = 0
    while True:
        count += 1
        zip_name = f"{base_name}{count}.{extension}"
        zip_path = os.path.join(base_path, zip_name)
        if not os.path.exists(zip_path):
            return zip_path

def generateSafeFilename(title):
    safeTitle = re.sub(r'[^a-zA-Z0-9_.-]', '_', title)
    safeTitle = unidecode(safeTitle)
    return safeTitle

def secondsToHms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return formatTime(int(hours), int(minutes), int(seconds))

def formatTime(hours, minutes, seconds):
    formattedTime = ""
    if hours > 0:
        formattedTime += f"{hours}:"
    formattedTime += f"{minutes:02d}:{seconds:02d}"
    return formattedTime
