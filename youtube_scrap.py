import scrapetube

videos = scrapetube.get_playlist("PLU_7CH0rKtkEKPbZP8b5rrquZky-VteXa")

for video in videos:
    print(video['videoId'])