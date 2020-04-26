## Network Study and the Impact of Social Bots on Public Opinion Polls  
##### CS5344 BigData Final Project - Group 2
  
In this project, we will firstly gather twitter data via both web scraping and existing dataset, then conduct a detection model to distinguish humans from bots. Based on that, we will conduct network analysis to identify the difference between bots and humans in social network. We also implement topic modeling and sentiment analysis aiming to understand trending topics of tweet content and explore the sentimental affecting mechanism from bots to humans.    


### Data Resource

1. ```tweets_json.json``` : Kaggle dataset - UK General Elections 2019 - Twitter replies  
This is our main dataset. To run the scripts, **download the dataset from the below link and *place it in the ```data/``` folder***:   
https://www.kaggle.com/moooozzz/uk-general-elections-2019-twitter-replies/download/d9605jnsmJzxiElRfmA2%2Fversions%2FwQuM603sN8oCEFqejtwX%2Ffiles%2Ftweets_json.json?datasetVersionNumber=1

2. ```data/final_data``` : Scrapped Tweets  
This folder contains tweet data in csv files collected by scraping historical tweets that were discussing the UK election 
or Brexit during that period with GetOldTweets3 python package. In addition to the scrapped tweets, the account’s information 
such as number of friend count, follower count are also collected using Twitter API with Tweepy. 

3. ```data/trainset.csv```: Train set for training xgboost model for social bots detection    
This labled data is created by us bying merging several open source datasets from 
https://botometer.iuni.iu.edu/bot-repository/datasets.html
  
4. ```data/label.csv``` :   
Label data predicted by the social bots detection model. used in network Analysis, Topic Modeling and Sentiment Analysis  
  
5. ```data/mp_party.csv``` :   
This dataset contains twitter account information of candidates for different British Parties manually labeled by us.
  
6. ```data/UK_Poll.xlsx``` :   
This data contains public poll results in a daily basis used in Sentiment Analysis  

  
### Code

1.```GetOldTweets.py``` :  
Python script for scraping data  

2.```SocialBotsDetection.ipynb``` :  
Social bots detection script including feature engineering, modeling and predicting labels  

3.```NetworkAnalysis.ipynb``` :  
Data preprocessing script for Network analysis (Algorithms and visualization part are via Gephi and not included in the code)  

4.```TopicModeling.ipynb``` :  
Topic modeling script including text preprocessing, EDA, modeling and visualization  

5.```SentimentAnalysis.ipynb``` :  
Sentiment analysis script including text preprocessing, modeling and visualization  
  
  

### Requirements/Packages

- Python3.x
- PySpark  
- findspark
- GetOldTweets3  
- sklearn  
- xgboost  
- nltk  
- gensim  
- textblob  
- pandas  
- numpy  
- emot  
- wget  
- pyLDAvis  
- wordcloud  
- plotly  
- matplotlib  
