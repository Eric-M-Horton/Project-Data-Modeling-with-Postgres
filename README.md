# Project: Data Modeling with Postgres

## Database Purpose

Sparkify has internal data, organized into JSON files, related to song and user data. To better improve their service Sparkify wants to organize this data into a database schema so it can be examined. Moreover, Sparkify would like the ability to run queries and create dashboards based on this data to better understand its significance. To help with this, they have enlisted the help of a data engineer to create a database structure and an ETL process to ingest their data.

## Database Design

The design of the database is centered around the songplayes table. For every time a song is played, a record in this table is created. There are then several related tables which provide further information about the song being played and who it's being played to. All linked by the ID values. These related tables include the song itself, the artist that made the song, the time the song was listened to, and the user that listened to the song. The purpose behind this design is to allow for flexibility in the queries being used as well as making intuitive sense to people trying to understand its structure.

## How to run

First, to create the tables navigate to the terminal and run 'python create_tables.py'. This will run the python script to create the tables defined by our database structure. Then, go back to the terminal and run 'python etl.py'. This will run the python script to ingest the JSON files and load them into the approprite tables.

### Important

If the files need to be ingested again, make sure to run the python create_tables.py command again to clear out the existing data.

If you want to ensure that the files have loaded correctly, open test.ipynb and use shift+enter, or the play button to run the individual cells.


## Files

The files are located in /data/log_data/2018/11/ and /data/song_data/

## Example 

Here is an example of a song file

num_songs:1
artist_id:"ARPFHN61187FB575F6"
artist_latitude:41.88415
artist_longitude:-87.63241
artist_location:"Chicago, IL"
artist_name:"Lupe Fiasco"
song_id:"SOWQTQZ12A58A7B63E"
title:"Streets On Fire (Explicit Album Version)"
duration:279.97995
year:0

Next, an example of a log file record

{"artist":"N.E.R.D. FEATURING MALICE","auth":"Logged In","firstName":"Jayden","gender":"M","itemInSession":0,"lastName":"Fox","length":288.9922,"level":"free","location":"New Orleans-Metairie, LA","method":"PUT","page":"NextSong","registration":1541033612796.0,"sessionId":184,"song":"Am I High (Feat. Malice)","status":200,"ts":1541121934796,"userAgent":"\"Mozilla\/5.0 (Windows NT 6.3; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"101"}

