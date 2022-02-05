from googleapiclient.discovery import build
import os

api_key = os.environ.get("youtube_api")
#api_key = 'API KEY'


def video_comments(video_id):
	# empty list for storing reply
	replies = []

	# creating youtube resource object
	youtube = build('youtube', 'v3',
					developerKey=api_key)

	# retrieve youtube video results
	video_response=youtube.commentThreads().list(
	part='snippet,replies',
	videoId=video_id
	).execute()

	# iterate video response
	while video_response:
		
		# extracting required info
		# from each result object
		for item in video_response['items']:
			
			# Extracting comments
			comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
			
			# counting number of reply of comment
			replycount = item['snippet']['totalReplyCount']

			# if reply is there
			if replycount>0:
				
				# iterate through all reply
				for reply in item['replies']['comments']:
					
					# Extract reply
					reply = reply['snippet']['textDisplay']
					
					# Store reply is list
					replies.append(reply)

			# print comment with list of reply
			print(comment, replies, end = '\n\n')

			# empty reply list
			replies = []

		# Again repeat
		if 'nextPageToken' in video_response:
			video_response = youtube.commentThreads().list(
					part = 'snippet,replies',
					videoId = video_id
				).execute()
		else:
			break

# Enter video id
video_id = "yYuHjpZj22o"

# Call function
video_comments(video_id)
