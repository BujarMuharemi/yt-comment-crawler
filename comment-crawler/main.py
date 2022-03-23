from googleapiclient.discovery import build
import json

"""
TODO: find out why it stops working after 2000 commentThreads
"""

# reading the API key from the env file
with open('comment-crawler\dev.env', 'r') as file:
    key = file.read().rstrip()

# creating a service object
youtube = build('youtube', 'v3', developerKey=key)

# search parameters
#videoId = "Vxl3EyA6JIE"
videoId = "1t9DAxeO6sA"
resultsPerPage = 100
noThreads=100
nextPageToken=None


i=0
counter=0
endOffPageTokens=False

while(not endOffPageTokens):    
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=videoId,
        maxResults=resultsPerPage,
        order="relevance",
        pageToken=nextPageToken
    )
    try:
        response = request.execute()
        
        # TODO: refactor this into a method
        for items in response['items']:
            rawItem = items['snippet']['topLevelComment']['snippet']['textOriginal']
            rawItem = rawItem.replace('\n', "")  # replace new lines
            rawItem = " ".join(rawItem.split())  # remove multiple spaces

            likeCount = items['snippet']['topLevelComment']['snippet']['likeCount']
            counter+=1
            # if(likeCount>10):
            print("#",counter, rawItem.strip(), "\t likeCount: ", likeCount)

            #print(response['nextPageToken'])
            if 'nextPageToken' in response:
                nextPageToken = response['nextPageToken']
            else:
                endOffPageTokens=True
                break

        #print("#######\n")
        i+=1

    except Exception as e:
        print(e)
        break


youtube.close()

#f = open("response.json", "a")
#f.write(json.dumps(response, sort_keys=True, indent=4))
#f.close()