# Spotify Project ETL
## Overview

I extracted my 50 recently played songs from [Spotify's Developer API](https://developer.spotify.com/console/get-recently-played/) via JSON. I then created a python function to perform data processing to convert the JSON file into a [Pandas](https://pandas.pydata.org/) dataframe. Last, I loaded the dataframe int a Postgres database.

## Extract: Spotify API
The extraction was done via Spotify's Developer utilizing the documentation. I used python's request package to download the data & saved a playlist.json file for later analysis.  

## Transformation: Pandas, Python
For data transformation, I wanted to extracted the song, artist, and timestamp data. Because the data was a list of nested dictionaries, I used python list slicing to identify the data needed & appened them to a list. From those lists, I created a dictionary to prep the data to create the pandas dataframe. Last, from the timestamp data, I created three additional columns: which included the date, time, and day of the week for analysis

## Load : Postgres 
[Psycopg2](https://pypi.org/project/psycopg2/) was used to create the engine to connect to the Postgres database. I then used the playlist_df.to_sql to ingest the data into the Postgres database.
