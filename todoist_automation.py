import os
import datetime
import json
from todoist_api_python.api import TodoistAPI
import googleapiclient.discovery
import googleapiclient.errors

# Load the API keys from a JSON file
with open('secret.json') as f:
    data = json.load(f)
yt_key = data['yt_api']
tdist_key = data['todoist_api']
sheet_id = data['sheet_id']

# Define the range of cells to read
range_name = 'Sheet1!A1:A'

# Read the values of the cells in the range
service = googleapiclient.discovery.build('sheets', 'v4', developerKey=yt_key)
result = service.spreadsheets().values().get(
    spreadsheetId=sheet_id, range=range_name).execute()
values = result.get('values', [])

# Define the main function
def main(channel_id):
    api_service_name = "youtube"
    api_version = "v3"
    
    api = TodoistAPI(tdist_key)

    # Get the latest videos from the YouTube channel
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=yt_key)
    
    # Define the date and time 24 hours ago
    now = datetime.datetime.utcnow()
    day_ago = now - datetime.timedelta(days=1)
    
    day_ago_str = day_ago.isoformat() + 'Z'
    
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=10,
        order="date",
        publishedAfter=day_ago_str
    )
    
    # Get the response from the YouTube API
    response = request.execute()
    
    # Extract the title and URL of each video from the response
    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        author = item['snippet']['channelTitle']
        url = f'https://www.youtube.com/watch?v={video_id}'
        try:
            task = api.add_task(content=f'[{title}]({url})', labels=[f'{author}'])
            print(author + " - " + title)
        except Exception as error:
            print(error)
        

# Define an empty array to store the IDs
ids = []

# Loop through the values and add any non-blank cells to the array
for row in values:
    if row:
        ids.append(row[0])
    else:
        break

for id in ids:
    main(id)
    