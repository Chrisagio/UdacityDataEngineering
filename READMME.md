# ETL Project for songplay data

The code of this project is accessing and reading data from two files (song data, log data) is creating a star schema with a fact table (songplays) and four dimension tables (artists,users, songs, time).
To create the songplays records the code is iterating through the rows of the log data file and extracts the selected values of the songplay table.
For the artist_id and the song_id in the songplays table, the code contains a select statement (song_select) which is running a join on the artists table and the songs table to check wether the record is containing the same artist_id.
Only if this is the case, the actual values of artist_id and song_id are being inserted into the songplays record.
If they are not matching the code inserts None for both artist_id and song_id.

## Data sources

The two data sources in use are:
1. Song data
2. Log data

The files contain the following attributes:

### song_data
- artist_id
- artist_latitude
- artist_location
- artist_longitude
- artist_name
- duration
- num_songs
- song_id
- title
- year

### log_data
- artist
- auth
- firstName
- gender
- itemInSession
- lastName
- length
- level
- location
- method
- page
- registration
- sessionId
- song
- status
- ts
- userAgent
- userId

## How to run the project

### Involved files

**1. sql_queries.py:** this file contains all the code to create and drop tables, select and join the artists and songs data, and eventually to insert the values into the individual tables.

**2. create_tables.py:** this file crates (or drops if already existing) the tables.

**3. etl.py: this file** contains the code to access and read the files, transforms the data and eventually executes the INSERT and SELECT statements needed to populate our tables

### Execution steps

1. Start with opening the terminal and running the **create_tables.py** file with the following command. This will create all the required tables of the star schema and drop tables if they existed before (e.g. when the project is re-run).

> `python create_tables.py`

2. Run the **etl.py** file to access and read the files, apply the required transformations and executing the INSERT and SELECT statements

> `python etl.py`
