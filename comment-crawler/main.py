from googleapiclient.discovery import build
import json, os
path = os.getcwd()


# TODO: read api key from env file
# TODO: check if commentThreads is the right option for this project

youtube = build('youtube', 'v3',developerKey='KEY Here')

request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId="2f9yv-T1QNM",
        maxResults=3,
        order="relevance"
    )
response = request.execute()
f = open("response.json", "a")
f.write(json.dumps(response, sort_keys=True, indent=4))
# TODO:loop threw all items 
print(response['items'][2]['snippet']['topLevelComment']['snippet']['textOriginal'])

f.close()

youtube.close()