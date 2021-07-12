import requests
import json
import pandas as pd
from secrets import *
import psycopg2
from sqlalchemy import create_engine
import os
# from config import config


# 1. **** EXTRACTION ****
# requests information for Spotify's API
url = 'https://api.spotify.com/v1/me/player/recently-played?limit=50'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

# request call for playlist data in json format
r = requests.get(url, headers=headers)

# json playlist data
playlist_data_json = r.json()

# save playlist data from request to json file for backup
# with open('playlist.json', 'w') as playlist_data:
#     json.dump(playlist_data_json, playlist_data)

# reading in the json file to do data transformation
with open('/Users/cianikaingram/Documents/DataEngineering_Portfolio/Spotify_Project/playlist.json', 'r') as playlist_file:
    playlist_data = json.load(playlist_file)



# 2. **** DATA TRANSFORMATION ****
# returning the song, artist, and timestamp data
song_names = []
artist_names = []
played_at_list = []

def data_transformation(playlist_data):
    for song in playlist_data['items']:
        song_names.append(song['track']['name'])
        artist_names.append(song['track']['album']['artists'][0]['name'])
        played_at_list.append(song['played_at'])

# create a dictionary from extracted json lists to prep for pandas dataframe
    playlist_dict = {
        'songs': song_names,
        'artists': artist_names,
        'timestamps': played_at_list
    }
# create pandas dataframe from playlist data
    playlist_df = pd.DataFrame(playlist_dict, columns = ['songs', 'artists', 'timestamps'])

# convert panda series to datetime
    df_timestamp = playlist_df['timestamps'] = pd.to_datetime(playlist_df['timestamps'])

# convert time zone from utc to eastern time zone & split datetime info into columns
    playlist_df['timestamps'] = df_timestamp.dt.tz_convert('US/Eastern')
    playlist_df['timestamp_date'] = df_timestamp.dt.strftime("%m-%d-%Y")
    playlist_df['timestamp_time'] = df_timestamp.dt.strftime("%I:%M %p")
    playlist_df['timestamp_day'] = df_timestamp.dt.strftime("%A")
    return playlist_df

playlist_df = data_transformation(playlist_data)

# 3. **** LOAD ****
# load into postgres database using psycopg2
engine = create_engine('postgresql+psycopg2://postgres:trublue6@localhost:5432/dataengineering')
connection = engine.connect()

playlist_df['timestamps'] = playlist_df['timestamps'].dt.strftime("%m-%d-%Y %H:%M:%S")
playlist_df.to_sql("spotify_playlist3", engine, if_exists='replace', index=False)

query2 = connection.execute("select * from spotify_playlist3;")
for result in query2.fetchall():
    print(result)



