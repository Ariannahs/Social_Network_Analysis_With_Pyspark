import GetOldTweets3 as got
import os 
import csv
import time
from datetime import datetime, timedelta

start = datetime.strptime("2019-12-11", "%Y-%m-%d")
end = datetime.strptime("2019-12-15", "%Y-%m-%d")
date_period = [start + timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_period:
    file_date = date.strftime("%Y_%m_%d")
    file_name = 'brexit_'+ file_date + '.csv'
    search_start_date = date.strftime("%Y-%m-%d")
    search_end_date = (date + timedelta(days=1)).strftime("%Y-%m-%d")
    
    print(file_name)
    print("search_start_date : ", search_start_date)
    print("search_end_date : ", search_end_date)

    # Open a new csv file with title row            
    twitter_file = open(file_name, 'w', newline='', encoding="utf-8")
    f=csv.writer(twitter_file)
    f.writerow(["id", "date", "username", "text", "retweets", "favorite", "Geo"])

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch("brexit").setSince(search_start_date).setUntil(search_end_date).setMaxTweets(10000)

    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for tweet in tweets : 
        t_id = tweet.id
        date = tweet.date
        username = tweet.username
        text = tweet.text
        retweet = tweet.retweets
        favorite = tweet.favorites 
        geo = tweet.geo
        # print(t_id, date, username, text)
        f.writerow([t_id, date, username, text])
    
    twitter_file.close() 
    time.sleep(7 * 60)