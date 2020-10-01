---
title: "HW4 : Create sqlite3 schema of Spotify Songs dataset in 3rd normal form (3NF)"
date: 2020-09-29
description: For Assignment 4
---

### Source data and code 
- The [Spotify Web API](https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv) provides artist, album, playlist, track and audio features data.
- [Source Code]() of this blog

### Database normalization
- Normalization is usually performed for reducing redundancy and preventing inconsistencies. 
- Three normal forms should be completed after the data normalization process.

#### First Normal Form (1NF)
- Table has primary key
- No composite values in each cell
- No repeating columns

*Get access to the data*
```python
import pandas as pd
raw = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv')
raw.sample(n = 5)
```
![1](/project/images/1NF_1.png) 
![2](/project/images/1nf_2.png)

After reading in the data, we can have a glance of it. There exists a primary key `track_id`. No repeating columns. Each cell only has one value. Therefore, the raw data is already a First Normal Form.

#### Second Normal Form (2NF)
- Remove partial dependencies

This dataset contains three main parts of information. 
- Track: `track_id`, `track_name`, `track_artist`, `track_popularity` and 12 audio features
- Album: `track_album_id`, `track_album_name`, `track_album_release_date`
- Playlist: `playlist_id`, `playlist_name`, `playlist_genre`, `playlist_subgenre`

In each of these three parts, columns only depend on the primary id of each part which generate partial dependencies. Therefore, I split the raw dataset into three tables and also create two link tables that could link splitted tables together.

```python
# split raw data
df_track = raw.iloc[:, np.r_[0:4, 11:23]].drop_duplicates()
df_album = raw.iloc[:, 4:7].drop_duplicates()
df_playlist = raw.iloc[:, [8,7,9,10]].drop_duplicates()

# generate link tables
df_track_album = raw.iloc[:, [0,4]].drop_duplicates()
df_track_playlist = raw.iloc[:, [0,8]].drop_duplicates()
```
#### Third Normal Form (3NF)
- Remove transitive dependency  

![3](/project/images/3nf.png)
In table `df_playlist`, we can see that the column `playlist_subgenre` only depends on the column `playlist_genre`, while `playlist_genre` depends on the primary key `playlist_id`. This is where transitive dependency occurs. Therefore, I create a new `df_playlist_` table that splits `playlist_subgenre` out. A new `df_subgenre` table is also created.

```python
df_playlist_ = df_playlist.iloc[:, 0:3].drop_duplicates()
df_subgenre = df_playlist.iloc[:, 2:4].drop_duplicates()
```

### Create sqlite3 schema
Command `df.to_sql()` helps me to convert pandas dataframes to sqlite3 tables. 

```python
import sqlite3
from sqlalchemy import create_engine
engine = create_engine('sqlite:///spotify.db', echo=False)

df_track.to_sql('track', con=engine)
df_album.to_sql('album', con=engine)
df_playlist_.to_sql('playlist', con=engine)
df_subgenre.to_sql('playlist_subgenre', con=engine)
df_track_album.to_sql('track_album', con=engine)
df_track_playlist.to_sql('track_playlist', con=engine)
```

### Find the names of all playlists that contain instrumentals

```python
q = """
SELECT DISTINCT(playlist_name)
FROM playlist
INNER JOIN track_playlist
    ON playlist.playlist_id = track_playlist.playlist_id
INNER JOIN track
    ON track_playlist.track_id = track.track_id
WHERE instrumentalness > 0.5
LIMIT 10;
"""
engine.execute(q).fetchall()
```

Part of results:
![4](/project/images/answer.png)