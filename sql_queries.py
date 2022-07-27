# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

##Songplays with columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL, start_time bigint, user_id text, level text, song_id text, artist_id text, session_id text, location text, user_agent text);")

##Users table with columns: user_id, first_name, last_name, gender, level
user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id text, first_name text, last_name text, gender text, level text);")

##Songs table with columns: song_id, title, artist_id, year, duration
song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id text, title text, artist_id text, year int, duration int);")

##Artists table with columns: artist_id, name, location, latitude, longitude
artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id text, name text, location text, latitude float(8), longitude float(8));")

##Time table with columns: start_time, hour, day, week, month, year, weekday
time_table_create = ("CREATE TABLE IF NOT EXISTS time (start_time time, hour int, day text, week int, month int, year int, weekday text);")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""")

user_table_insert = ("""INSERT INTO users (user_id,first_name,last_name,gender,level) VALUES (%s,%s,%s,%s,%s)""")

song_table_insert = ("""INSERT INTO songs (song_id,title,artist_id,year,duration) VALUES (%s,%s,%s,%s,%s)""")

artist_table_insert = ("""INSERT INTO artists (artist_id,name,location,latitude,longitude) VALUES (%s,%s,%s,%s,%s)""")


time_table_insert = ("""INSERT INTO time (start_time,hour,day,week,month,year,weekday) VALUES (%s,%s,%s,%s,%s,%s,%s)""")

# FIND SONGS

song_select = ("""SELECT artists.artist_id,songs.song_id FROM (artists JOIN songs ON artists.artist_id = songs.artist_id)WHERE songs.title=%s AND artists.name=%s AND songs.duration=%s;""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
