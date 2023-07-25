import googleapiclient.discovery
import dataHandler as dh

API_KEY = dh.readData()

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

def getVideosFromPlaylist(playlistLink, maxResults):
    videos = []
    total_results = 0
    nextPage_token = None
    playlistId = playlistLinkSplit(playlistLink)

    while True:
        remaining_results = maxResults - total_results if maxResults else 50
        results_to_fetch = min(remaining_results, 50)

        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlistId,
            maxResults=results_to_fetch,
            pageToken=nextPage_token,
        )
        response = request.execute()

        for item in response["items"]:
            video_id = item["snippet"]["resourceId"]["videoId"]
            video_title = item["snippet"]["title"]
            videos.append({"video_id": video_id, "title": video_title})
            total_results += 1

        nextPage_token = response.get("nextPageToken")

        if not nextPage_token or (maxResults and total_results >= maxResults):
            break
    return videos

def playlistLinkSplit(string):
    playlistId = string.split("list=")
    if len(playlistId) > 1:
        playlistId = playlistId[1].split("&")
    return playlistId[0]
