# DROP TABLES

songplay_table_drop = "drop table if exists songplays cascade;"
user_table_drop = "drop table if exists users cascade"
song_table_drop = "drop table if exists songs cascade"
artist_table_drop = "drop table if exists artist cascade"
time_table_drop = "drop table if exists time cascade"

# CREATE TABLES

songplay_table_create = (
    "create table if not exists songplays ("
    "songplay_id SERIAL PRIMARY KEY,"
    " start_time varchar references time(start_time),"
    " user_id integer references users(user_id),"
    " level varchar,"
    " song_id varchar references songs(song_id),"
    " artist_id varchar references artists(artist_id),"
    " session_id varchar,"
    " location varchar,"
    " user_agent varchar"
    ")")

user_table_create = (
    "create table if not exists users("
    "user_id integer not null CONSTRAINT user_id PRIMARY KEY,"
    "first_name varchar,"
    "last_name varchar,"
    "gender varchar,"
    "level varchar"
    ")")

song_table_create = (
    "create table if not exists songs ("
    "song_id varchar not null CONSTRAINT song_id PRIMARY KEY,"
    "title varchar,"
    "artist_id varchar references artists(artist_id),"
    "year integer,"
    "duration numeric"
    ")")

artist_table_create = (
    "create table if not exists artists("
    "artist_id varchar not null CONSTRAINT artist_id PRIMARY KEY,"
    "name varchar,"
    "location varchar,"
    "latitude varchar,"
    "longitude varchar)")

time_table_create = (
    "create table if not exists time("
    "start_time varchar CONSTRAINT start_time PRIMARY KEY,"
    "hour varchar,"
    "day varchar,"
    "week varchar,"
    "month varchar,"
    "year varchar,"
    "weekday varchar)")

# INSERT RECORDS

songplay_table_insert = (
    "insert into songplays("
    "start_time,"
    "user_id,"
    "level,"
    "song_id,"
    "artist_id,"
    "session_id,"
    "location,"
    "user_agent) values (%s,%s,%s,%s,%s,%s,%s,%s)")

user_table_insert = (
    "insert into users("
    "user_id,"
    "first_name,"
    "last_name,"
    "gender,"
    "level) values (%s,%s,%s,%s,%s) on conflict (user_id) do nothing")

song_table_insert = (
    "insert into songs("
    "song_id,"
    "title,"
    "artist_id,"
    "year,"
    "duration) values (%s,%s,%s,%s,%s) on conflict (song_id) do nothing")

artist_table_insert = (
    "insert into artists("
    "artist_id,"
    "name,"
    "location,"
    "latitude,"
    "longitude) values (%s,%s,%s,%s,%s) on conflict (artist_id) do nothing")

time_table_insert = (
    "insert into time("
    "start_time,"
    "hour,"
    "day,"
    "week,"
    "month,"
    "year,"
    "weekday) values (%s,%s,%s,%s,%s,%s,%s) on conflict (start_time) do nothing")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, songs.artist_id 
    FROM songs s, artists a
    WHERE 1=1
    and s.artist_id = a.artist_id
    songs.title=%s 
    AND artists.name=%s 
    AND songs.duration=%s""")

# QUERY LISTS

create_table_queries = [user_table_create,artist_table_create,song_table_create,
                        time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
