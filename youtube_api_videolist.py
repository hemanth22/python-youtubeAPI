import googleapiclient.discovery
import os

playlist_id = "PLU_7CH0rKtkEKPbZP8b5rrquZky-VteXa"

api_key = os.environ.get("youtube_api")

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

request = youtube.playlistItems().list(
    part = "snippet",
    playlistId = playlist_id,
    maxResults = 50
)
response = request.execute()

playlist_items = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)

print(f"total: {len(playlist_items)}")
print(playlist_items)