# TWITTER PROJECT 

I utilized Twitters API via [Tweepy](https://www.tweepy.org/) to access 2,000 tweets since 2020-01-01 that contained the #DataEngineering or #dataengineering hashtag.  I used loops & the Pandas package for Data Transformation & the Matplotlib package for Data Visualization.

## DataTransformation 
I iterated over each tweet & appended them to list. I iterated over the list of tweets & extracted the hashtags. I noticed that because some tweets had multiple hashtags, they were stored in a list of nested dictionaries. I then iterated over each hashtag in the nested dictionary and appended them to an individual list of hashtags.

Finally, to analyze and tally the hashtags, I put the list of hashtags in to a pandas DataFrame, examined the count & created a data visualization that displayed the count of #dataengineering hashtag, along with the top four hashtags used when the #dataengineering was mentioned.

## Data Visualization
Pandas, Matplotlib


