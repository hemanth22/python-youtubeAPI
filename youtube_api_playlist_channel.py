import googleapiclient.discovery

channel_id = "UC1udnO-W6gpR9qzleJ5SDKw"

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "youtube_api")

request = youtube.playlists().list(
    part = "snippet",
    channelId = channel_id,
    maxResults = 50
)
response = request.execute()

playlists = []
while request is not None:
    response = request.execute()
    playlists += response["items"]
    request = youtube.playlists().list_next(request, response)

print(f"total: {len(playlists)}")
print(playlists)