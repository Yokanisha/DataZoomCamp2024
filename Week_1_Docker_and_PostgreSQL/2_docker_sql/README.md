in .bashrc
export PATH="${PATH}:/c/users/armut/appdata/local/packages/pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0/localcache/local-packages/python39/site-packages


in script ordner in bash
export PATH=$PATH:"/c/Users/Armut/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/Scripts"



//create the container
winpty docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5431:5432 \
  postgres:13

//first bash - start the container
winpty docker start -i 6b6f5aa66c239f7e7fc6e77c30c1a124e3eaa55912b4865eb1fda771a54aeb44




//Sec bash
winpty pgcli -h localhost -p 5431 -u root -d ny_taxi
Password for root: root


//we dont need postgrSQL to download. We have Docker. We can just pull a Docker image that contaisn the tool.

docker pull dpage/pgadmin4

winpty docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4

//Postgres and pgAdmin are in different container. SO we need to connect them to register in pgAdmins erver with postgr names


//need to start noth container (see name)
//Database
winpty docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5431:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13

//PGAdmin
winpty docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin-2 \
  dpage/pgadmin4


----------------------------------------------------

//Didn't work for me so I used local folder - see one below
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
winpty python3 ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5431 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL}

// notice, it is a CSV data
URL="D:/DE-ZoomCamp/week_1_basics_n_setup/2_docker_sql/yellow_tripdata_2019-01.csv"
winpty python3 ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5431 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --csv_path="${URL}"



winpty docker build -t taxi_ingest:v001 .


winpty docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url="${URL}"

--------------------- so it is faster --------------------- 

run in git bash: python -m hhtp.server

open another git bash:

It works because we already downloaded the file:

make sure it is downloaded in the correct file!!

URL="http://192.168.0.103:8000/yellow_tripdata_2021-01.csv"

winpty docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url="${URL}"

