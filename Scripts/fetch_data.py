import os 
import requests
from dotenv import load_dotenv
import json

#load env variables from .env file 
load_dotenv()

API_KEY=os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID=os.getenv("CHANNEL_ID")

headers = {
    "User-Agent": "Mozilla/5.0"
}

# YOUTUBE API URL
url = "https://www.googleapis.com/youtube/v3/channels"
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
VIDEO_URL = "https://www.googleapis.com/youtube/v3/videos"
playlists_URL = "https://www.googleapis.com/youtube/v3/playlists"
playlist_item_URL = "https://www.googleapis.com/youtube/v3/playlistitems"

def fetch_video_id(channel_id,API_key,):
    Search_parameter = {
        "part": "snippet",
        "channelId": channel_id,
        "key": API_key,
        "order": "date", # will give by uploaded date
        "maxResults": 50
    }

    response = requests.get(SEARCH_URL, params= Search_parameter,headers=headers)

    if response.status_code==200:
        data=response.json()
        #creating a empty list to store the Video IDs
        video_ids =[]
        # using for loop to search in data dictionary
        for item in data["items"]:
            if "videoId" in item["id"]: #checking if video_id is present i.e checking for video and it is not playlist
                video_id=item["id"]["videoId"] #stroring the video id in a variable
                video_ids.append(video_id) # appending to the list
        return video_ids
    else:
        print("Error fetching video IDs:", response.status_code, response.text)
        return []
    
#fetch video detais(statistics)
def fetch_video_details(video_ids,api_key):
    video_parameter={
        "part" : "statistics,snippet",
        "id" :",".join(video_ids), #since it is a list so we have given the video id in comma seprated 
        "key": api_key
    }

    response = requests.get(VIDEO_URL,params=video_parameter,headers=headers)
    
    if response.status_code==200:
        return response.json()
    else:
        print("error fetching video details", response.status_code,response.text)
        return[]
    

def main():
    video_id=fetch_video_id(CHANNEL_ID,API_KEY)
    if video_id:
        print("video found",len(video_id))

        video_data=fetch_video_details(video_id,API_KEY)
        #print(video_data)
        with open("../Data/Raw_data/video_data.json","w") as json_file:
            json.dump(video_data,json_file, indent=4)
        print("video datails saved in json file")
    else:
        print("no video id/data found")

if __name__=="__main__":
    main()

    




'''try:
    #checking if the requests made was suceessful
    if response.status_code==200:
        
        #this line will give the response code
        #print(response)
        #if we want raw response to be printed 
        #print(response.text)
        data=response.json()    #convert raw json string into python dictionary
        #print(data)

        snippet= data["items"][0]["snippet"]
        stats=data["items"][0]["statistics"]
        print("Channel Title:", snippet["title"])
        print("Channel customURL:", snippet["customUrl"])
        print("Subscribers:", stats.get("subscriberCount"))
        print("Total Views:", stats.get("viewCount"))
        print("Video Count:", stats.get("videoCount"))
except Exception as e:
        print("Failed to fetch data:", response.status_code, response.text)'''
        