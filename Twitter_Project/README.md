# TWITTER PROJECT 


I utilized Twitters API via Tweepy https://www.tweepy.org/ to access 2,000 tweets since 2020-01-01 that contained the #DataEngineering of #dataengineering hashtag.  I used loops & the Pandas package for Data Transformation & the Matplotlib package for Data Visualization.

## DataTransformation 
I iterated over each tweet & appended them to list. I iterated over list of tweets & extracted the hashtags. I noticed that because some tweets had multiple hashtags, they were stored in a list of nested dictionaries. I then iterated overreach hashtag in the nested dictionary and appended them to an individual list.

To analyze tally the hashtags, I put the list of hashtags in to a pandas DataFrame, examined the count & created a data visualization that display the count of #dataengineering hashtag along with the top hour hashtags used when the #dataengineering was mentioned.

## Data Visualization
Pandas, Matplotlib


