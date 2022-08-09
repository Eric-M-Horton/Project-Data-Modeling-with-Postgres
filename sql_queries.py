# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS times;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
(
    songplay_id serial primary key,
    start_time timestamp NOT NULL,
    userid INT NOT NULL,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id varchar,
    location varchar,
    user_agent varchar
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users 
(
    userid INT primary key,
    firstName varchar,
    lastName varchar,
    gender varchar,
    level varchar
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs 
(
    song_id varchar primary key NOT NULL,
    title text NOT NULL,
    artist_id varchar,
    year int,
    duration float NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists 
(
    artist_id varchar primary key,
    name varchar NOT NULL,
    location varchar,
    latitude float,
    longitude float
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
(
    start_time timestamp PRIMARY KEY,
    hour int,
    day varchar,
    week int,
    month varchar,
    year int,
    weekday varchar
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays 
(
    start_time,
    userid,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO USERS 
(
    userid,
    firstName,
    lastName,
    gender,
    level
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (userid) DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs 
(
    song_id,
    title,
    artist_id,
    duration
)
VALUES (%s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists 
(
    artist_id,
    name,
    location,
    latitude,
    longitude
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time 
(
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

# FIND SONGS



song_select = ("""
select songs.song_id, artists.artist_id
from songs
join artists
on songs.artist_id = artists.artist_id
where songs.title = %s and artists.name = %s and songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]