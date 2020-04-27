## Network Study on the Impact of Social Bots on Public Opinion Polls  
   
### Introduction  
  
In this project, we use multiple twitter data source via web scraping and existing 
datasets. We first **implement Xgboost model to detect social bots**. Then, we 
use the labels derived from the social bots detection to conduct three parallel 
studies including **network analysis using Hubs and Authorities Algorithm (HITS), 
topic modeling using LSA, NMF, LDA and sentiment analysis using textblob** 
in order to identify the difference between bots and humans in terms of importance 
scores, topic trends and sentimental affecting mechanism.    

The overall pipeline works like:  
**1. Data Scraping => 2. Social Bots Detection => 3. Network Analysis & Topic Modeling & Sentiment Analysis**  

  
### Data Resource

Main data source: *Kaggle UK General Elections 2019 - Twitter replies*    
  
This is a scraped dataset using Twitter API contains more than 300, 000 tweets collected from 16 Nov to 14 Dec concerning the UK 2019 General Election. This is a JSON dump of all the tweets, including full metadata. Each part of the file is one tweet. Refer to the link: 
https://www.kaggle.com/moooozzz/uk-general-elections-2019-twitter-replies/download/d9605jnsmJzxiElRfmA2%2Fversions%2FwQuM603sN8oCEFqejtwX%2Ffiles%2Ftweets_json.json?datasetVersionNumber=1

Other data source:  
1) Scrapped Tweets: scraped data containing historical tweets that were discussing the UK election or Brexit during that period with GetOldTweets3 python package. In addition to the scrapped tweets, the account’s information such as number of friend count, follower count are also collected using Twitter API with Tweepy.   
2) trainset for social bots detection: labled data created by us bying merging several open source datasets from 
https://botometer.iuni.iu.edu/bot-repository/datasets.html  
3) mp party dataset: scarped data containing twitter account information of candidates. Parties information are manually labeled by us.   
4) UK Poll dataset: scarped data containing public poll results in a daily basis used in Sentiment Analysis.  

  
  
### Code

1. ```GetOldTweets.py``` :  
Python script for scraping data  

2. ```SocialBotsDetection.ipynb``` :  
Social bots detection script including feature engineering, modeling and predicting 
labels  

3. ```NetworkAnalysis.ipynb``` :  
Data preprocessing script for Network analysis (Algorithms and visualization part 
are via Gephi and not included in the code)  

4. ```TopicModeling.ipynb``` :  
Topic modeling script including text preprocessing, EDA, modeling and visualization  

5. ```SentimentAnalysis.ipynb``` :  
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
