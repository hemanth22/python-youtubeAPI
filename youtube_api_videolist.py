import googleapiclient.discovery

playlist_id = "PLU_7CH0rKtkEKPbZP8b5rrquZky-VteXa"

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "youtube_api")

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