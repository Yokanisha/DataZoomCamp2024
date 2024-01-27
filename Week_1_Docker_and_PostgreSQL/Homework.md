## Module 1 Homework

## Docker & SQL

In this homework we'll prepare the environment 
and practice with Docker and SQL


## Question 1. Knowing docker tags

Run the command to get information on Docker 

```docker --help```

Now run the command to get help on the "docker build" command:

```docker build --help```

Do the same for "docker run".

Which tag has the following text? - *Automatically remove the container when it exits* 

- `--delete` 
- `--rc`
- `--rmc`
- `--rm` :thumbsup:


## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use ```pip list``` ). 

What is version of the package *wheel* ?

- 0.42.0 :thumbsup:
- 1.0.0
- 23.0.1
- 58.1.0

### Answer
```
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_1_basics_n_setup/2_docker_sql
$ winpty docker run -it --entrypoint=bash python:3.9
root@cf9f6318b6f4:/# pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 58.1.0
wheel      0.42.0

[notice] A new release of pip is available: 23.0.1 -> 23.3.2
[notice] To update, run: pip install --upgrade pip
root@cf9f6318b6f4:/#
```



# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from September 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)

### Approach

I need to check if the column names are the same or different:
```
import pandas as pd
df = pd.read_csv('D:/DE-ZoomCamp/week_1_basics_n_setup/2_docker_sql/Daten/green_tripdata_2019-09.csv', nrows=100)
df.head()
```
The names of the column two `lpep_pickup_datetime` and column three `lpep_dropoff_datetime` were different. So I need to change the names of my `ingest_data.py` file.

After I can run the follow script:

```
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"
winpty docker build -t taxi_ingest:v001 .
winpty docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_trips \
    --url="${URL}"
```
The file `https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv` is already in the database from the previous tutorial.

## Question 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- 15767 :thumbsup:
- 15612
- 15859
- 89009

### Approach
Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format DATETIME (YYYY-MM-DD HH:MI:SS) and not in DATE (YYYY-MM-DD).

```
SELECT COUNT(*) FROM green_taxi_trips
WHERE DATE(lpep_pickup_datetime) = '2019-09-18';
```


## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

- 2019-09-18
- 2019-09-16
- 2019-09-26
- 2019-09-21


## Question 5. Three biggest pick up Boroughs

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
 
- "Brooklyn" "Manhattan" "Queens"
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens" 
- "Brooklyn" "Queens" "Staten Island"


## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- JFK Airport
- Long Island City/Queens Plaza