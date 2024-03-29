from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import re
import os

# Your YouTube API key
API_KEY = os.environ.get('YOUTUBE_API_KEY')

# Function to fetch subtitles of a YouTube video
def get_video_subtitles(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles = ' '.join([line['text'] for line in transcript])
        return subtitles
    except Exception as e:
        print(f"Error fetching subtitles: {e}")
        return None

# Function to fetch video details
def get_video_details(video_id):
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        request = youtube.videos().list(
            part='snippet',
            id=video_id
        )
        response = request.execute()
        return response['items'][0]['snippet']
    except Exception as e:
        print(f"Error fetching video details: {e}")
        return None

def get_video_id(video_link):
    # Regular expression pattern to match YouTube video IDs
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    
    # Attempt to find the video ID in the link
    match = re.search(pattern, video_link)
    if match:
        return match.group(1)
    else:
        print("Invalid YouTube video link.")
        return None

# Example usage
if __name__ == '__main__':
    video_link = input("Enter YouTube video link: ")
    video_id = get_video_id(video_link)
    if video_id:
        print("Video ID:", video_id)

    # Get video details
    video_details = get_video_details(video_id)
    if video_details:
        print(f"Title: {video_details['title']}")
        print(f"Description: {video_details['description']}")
    
    # Get video subtitles
    subtitles = get_video_subtitles(video_id)
    if subtitles:
        print("\nSubtitles:")
        print(subtitles)
