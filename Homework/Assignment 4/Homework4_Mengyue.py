#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import sqlite3


# In[2]:


raw = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv')


# In[38]:


raw.sample(n=5)


# In[11]:


raw.sample(n = 10).iloc[1:10,1:6]


# In[5]:


# 1NF: no composite entries, no repeated columns
# raw data is alreay 1NF form


# In[ ]:


# 2NF: break partial dependencies.


# In[33]:


df_track = raw.iloc[:, np.r_[0:4, 11:23]].drop_duplicates()
df_track


# In[34]:


df_album = raw.iloc[:, 4:7].drop_duplicates()
df_album


# In[39]:


df_playlist = raw.iloc[:, [8,7,9,10]].drop_duplicates()
df_playlist.sample(n=10)


# In[71]:


df_playlist.sample(n=5)


# In[36]:


# create link tables
df_track_album = raw.iloc[:, [0,4]].drop_duplicates()
df_track_album


# In[37]:


df_track_playlist = raw.iloc[:, [0,8]].drop_duplicates()
df_track_playlist


# In[40]:


# 3NF: remove transitive dependency
# playlist_subgenre only depends on playlist_genre


# In[41]:


df_playlist_ = df_playlist.iloc[:, 0:3].drop_duplicates()
df_playlist_.sample()


# In[43]:


df_subgenre = df_playlist.iloc[:, 2:4].drop_duplicates()
df_subgenre


# In[ ]:


# convert dataframe to sql table
# create sql schema


# In[49]:


from sqlalchemy import create_engine

engine = create_engine('sqlite:///spotify.db', echo=False)


# In[50]:


df_track.to_sql('track', con=engine)


# In[51]:


df_album.to_sql('album', con=engine)


# In[52]:


df_playlist_.to_sql('playlist', con=engine)
df_subgenre.to_sql('playlist_subgenre', con=engine)
df_track_album.to_sql('track_album', con=engine)
df_track_playlist.to_sql('track_playlist', con=engine)


# In[73]:


# find the names of all playlists that contain instrumentals
q = """
SELECT DISTINCT(playlist_name)
FROM playlist
INNER JOIN track_playlist
    ON playlist.playlist_id = track_playlist.playlist_id
INNER JOIN track
    ON track_playlist.track_id = track.track_id
WHERE instrumentalness > 0.5;
"""
engine.execute(q).fetchall()

