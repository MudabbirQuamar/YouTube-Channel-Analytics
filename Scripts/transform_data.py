import pandas as pd
import json
from datetime import datetime
import pytz
import os

#funtion to extract the data from json file
def extract_data_from_json():
    #we are getting the absolute path of current file
    current_directory = os.path.dirname(os.path.abspath(__file__))

    #getting to the json file path
    json_path = os.path.join(current_directory,"../Data/Raw_data/video_data.json")

    #normalizing the path 
    json_path = os.path.normpath(json_path)

    #print(json_path)
    with open(json_path,"r") as jsonfile:
        data=json.load(jsonfile)
    # i have loaded the data from json file and converted it to python object (dictionary)
    # now we will normalize the data(i.e. python objecti.e. dictionary )
    # we can not convert directly as it is nested dictionary
    # we will be using pandas json.normalize function

    structured_data=pd.json_normalize(
        data["items"],
        sep="_",
    )
    return structured_data

def cleaning_data(structured_data): #this function is to clean the data
    # as by default everything in json(YT response) is string so we need to change the data type
    structured_data["PublishedAt"]=pd.to_datetime(structured_data["snippet_publishedAt"])
    structured_data["Title"]=structured_data["snippet_title"]
    structured_data["Tags"]=structured_data["snippet_tags"]
    structured_data["ViewsCount"]=structured_data["statistics_viewCount"].astype(int)
    structured_data["LikesCount"]=structured_data["statistics_likeCount"].astype(int)
    structured_data["FavouriteCount"]=structured_data["statistics_favoriteCount"].astype(int)
    structured_data["CommentsCount"]=structured_data["statistics_commentCount"].astype(int)
    clean_data = structured_data[["Title","Tags","PublishedAt","ViewsCount","LikesCount","FavouriteCount","CommentsCount"]].copy()
    return clean_data


#this function will calculate the no of days the video is published and engagement rate also, some more transformation
def transform_data(clean_data):
    #datetime.now() return datetime of type tz- naive which does not know the time zone so i make it tz- aware time zone using pytz module
    clean_data["Days_Since_Published"] = (datetime.now(pytz.timezone('Asia/Kolkata'))- clean_data["PublishedAt"]).dt.days
    #ADDING a column engagement_rate to the data frame to give the engagement rate (L+C)/V
    clean_data["engagement_rate"] = ((clean_data["LikesCount"]+clean_data["CommentsCount"])/clean_data["ViewsCount"])*100
    transformed_data=clean_data[["Title","Tags","PublishedAt","ViewsCount","LikesCount","FavouriteCount","CommentsCount","Days_Since_Published","engagement_rate"]]
    # i am calculating the views per day each video is getting 
    transformed_data["Views_velocity "]=round(transformed_data["ViewsCount"]/transformed_data["Days_Since_Published"],2)
    #tranformed_data datafreame has 10 coloumns 2 which i Made and 7 from clean data
    return transformed_data


def tag_analysis(transformed_data):
    #here I made a new data frame with two coloumns and used the explode funtion to transform the data into multiple row with each
    #row having 1 tags and engagement rate
    #tag_data_frame = transformed_data[["Tags","engagement_rate"]].explode("Tags")
    #making a column has tag to check the video has tag or not
    #.copy() is to make a seprate copy of the Df as i need to modiyf
    tag_data_frame = transformed_data[["Tags","engagement_rate","ViewsCount"]].copy()
    tag_data_frame["HasTag"]=tag_data_frame["Tags"].apply(lambda x: isinstance(x,list) and len(x) > 0)
    # this line of code will make the tags in lower case and strip the trailing spaces
    #tag_data_frame["Tags"] = tag_data_frame["Tags"].str.lower().str.strip()

    # now I have added the hastag colomn i will grop it by hastag colomn
    tag_data_frame=tag_data_frame.groupby("HasTag")["engagement_rate"].mean().reset_index()
    return tag_data_frame

    



'''print(data)
    #pd.json_normalize(data=data)
    #print(data.keys())
    #print(data["items"][0])
    with open("after_load","w") as dataload:
        json.dump(data,dataload,indent=4)'''

'''if __name__=="__main__":
    structured_data = extract_data_from_json()
    #print(structured_data)
    clean_data = cleaning_data(structured_data)
    #print(clean_data)
    transformed_data = transform_data(clean_data)
    #print(transformed_data[["LikesCount","CommentsCount","ViewsCount","FavouriteCount","engagement_rate"]])
    #print(transformed_data)
    tag_analyzed_data = tag_analysis(transformed_data)'''
    

