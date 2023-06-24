import os
import json
from todoist_api_python.api import TodoistAPI
import googleapiclient.discovery
import googleapiclient.errors

def main():
    api_service_name = "youtube"
    api_version = "v3"

    # Load the API key from a JSON file
    with open('secret.json') as f:
        data = json.load(f)
    yt_key = data['yt_api']
    tdist_key = data['todoist_api']
    
    api = TodoistAPI(tdist_key)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=yt_key)

    request = youtube.search().list(
        part="snippet",
        channelId="UCsBjURrPoezykLs9EqgamOA",
        maxResults=4,
        order="date"
    )
    
    response = request.execute()
    
        # Print the title and URL of each video
    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        url = f'https://www.youtube.com/watch?v={video_id}'
        print(f'Title: {title}')
        print(f'URL: {url}')
        # [This text will be hyperlinked](http://todoist.com/)
    try:
        task = api.add_task(content=f'[{title}]({url})')
        print(task)
    except Exception as error:
        print(error)
        
if __name__ == "__main__":
    main()
