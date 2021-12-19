from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

with open('cred.json') as cred:
    key = json.load(cred)

DEVELOPER_KEY = key['API_KEY']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

required = [
    "title",
    "description",
    "publishedAt",
]

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=options['query'],
        part='id,snippet',
        maxResults=options['max_result'],
        order='date',
    ).execute()

    videos = dict()

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            temp = dict()
            for req in required:
                temp[req] = search_result['snippet'][req]
            temp['thumbnail'] = search_result['snippet']['thumbnails']['default']['url']
            temp["video_url"] = "".join(['https://www.youtube.com/watch?v=', search_result['id']['videoId']])
            videos[search_result['id']['videoId']] = temp
    
    return videos

if __name__ == '__main__':
    args = {
        "query" : "Google",
        "max_result": 25,
    }
    try:
        youtube_search(args)
    except HttpError as e:
        print ('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)) 