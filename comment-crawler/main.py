from googleapiclient.discovery import build
import csv
import os


key = os.environ['YT_C2_API_KEY']

f = open('./csv_file.csv', 'w',encoding="utf-8",newline='')
writer = csv.writer(f,delimiter='╬') #delimiter needs to be special alt code. So commas the comments, don't break parsing later

"""
TODO: find out why it stops working after 2000 commentThreads
"""

# creating a service object
youtube = build('youtube', 'v3', developerKey=key)

# search parameters
#videoId = "Vxl3EyA6JIE"
#videoId = "6ywR3OU11n4" #it should return 6 comment threads
videoId = os.environ["YT_VID_ID"]
#6ywR3OU11n4

resultsPerPage = 100
noThreads=100
nextPageToken=None


i=0
counter=0
totalCommentsCnt=0
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
        totalCommentsCnt+=len(response['items'])

        # TODO: refactor this into a method
        for items in response['items']:
            #print(items,"\n####")
            rawItem = items['snippet']['topLevelComment']['snippet']['textOriginal']
            rawItem = rawItem.replace('\n', "")  # replace new lines
            rawItem = " ".join(rawItem.split())  # remove multiple spaces

            likeCount = items['snippet']['topLevelComment']['snippet']['likeCount']
            replies = items['snippet']['totalReplyCount']
            totalCommentsCnt+=replies
            counter+=1
            #if(likeCount>10):
            #print("#",counter, rawItem.strip(), "\t likeCount: ", likeCount,"\t Replies:",replies)

            row = [rawItem.strip(),likeCount,replies]
            writer.writerow(row)

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
print(totalCommentsCnt+1)
f.close()


#f = open("response.json", "a")
#f.write(json.dumps(response, sort_keys=True, indent=4))
#f.close()