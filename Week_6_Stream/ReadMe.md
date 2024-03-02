# Preperation

- Open in pycharm a new projekt. 
- Go to folder python -> docker -> kafka and create a `docker-compose.yml` file. #make it to a link
- In bash go to folder kafka and run `docker network create kafka-spark-network`
  - you will see `kafka-spark-network     bridge`.
    
```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/docker/kafka
$ docker network ls
NETWORK ID     NAME                    DRIVER    SCOPE
4f47e77b97cd   2_docker_sql_default    bridge    local
10e99b9444e9   bridge                  bridge    local
27ada8351254   host                    host      local
658cff95a410   kafka-spark-network     bridge    local
fbfd869a4aaa   mage-zoomcamp_default   bridge    local
1b5633ecace3   none                    null      local
3b7e93627564   pg-network              bridge    local
```

- run docker compose up -d

- run python producer.py
 - If you get an error like this (below), do `How to fix: ModuleNotFoundError: No module named 'kafka'`.

```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/json_example
$ python3 producer.py
Traceback (most recent call last):
  File "D:\DE-ZoomCamp\week_6_stream_python\python\json_example\producer.py", line 4, in <module>
    from kafka import KafkaProducer
ModuleNotFoundError: No module named 'kafka'
```

### How to fix: ModuleNotFoundError: Nomodule named 'kafka'

- Navigate to your project file and type
```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python
$ python -m venv env
(env)
```
- Make sure env is activated in windows

```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python
$ source env/Scripts/activate
(env)
```

- run
```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python
$ ./env/Scripts/activate
(env)
```

- See what do you have. If you don't have kafka in the list, you need to install
```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/json_example
$ pip list
Package    Version
---------- -------
pip        22.0.4
setuptools 58.1.0
WARNING: You are using pip version 22.0.4; however, version 24.0 is available.
You should consider upgrading via the 'D:\DE-ZoomCamp\week_6_stream_python\python\env\Scripts\python.exe -m pip install --upgrade pip' command.
(env)

```
- To install run `pip install kafka-python`
- Navigate to your producer.py file and run `python producer.py`
- Now, it should work.
- for deactivate run `deactivate`
- To activate it (you'll need to run it every time you need the virtual env): `./env/Scripts/activate`

### Run scripts
- Run `python producer.py`
```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/json_example
$ python producer.py
Record 238 successfully produced at offset 0
Record 138 successfully produced at offset 1
Record 230 successfully produced at offset 2
Record 88 successfully produced at offset 3
Record 37 successfully produced at offset 4
Record 140 successfully produced at offset 5
Record 137 successfully produced at offset 6
...
```
- Run `python consumer.py`
```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/json_example
$ python consumer.py
Consuming from Kafka started
Available topics to consume:  {'rides_json'}
238 Ride: {'vendor_id': '1', 'tpep_pickup_datetime': (datetime.datetime(2020, 7, 1, 0, 25, 32),), 'tpep_dropoff_datetime': (datetime.datetime(2020, 7, 1, 0, 33, 39),), 'passenger_count': 1, 'trip_distance': Decimal('1.50'), 'rate_code_id': 1, 'store_and_fwd_flag': 'N', 'pu_location_id': 238, 'do_location_id': 75, 'payment_type': '2', 'fare_amount': Decimal('8'), 'extra': Decimal('0.5'), 'mta_tax': Decimal('0.5'), 'tip_amount': Decimal('0'), 'tolls_amount': Decimal('0'), 'improvement_surcharge': Decimal('0.3'), 'total_amount': Decimal('9.3'), 'congestion_surcharge': Decimal('0')}
138 Ride: {'vendor_id': '1', 'tpep_pickup_datetime': (datetime.datetime(2020, 7, 1, 0, 3, 19),), 'tpep_dropoff_datetime': (datetime.datetime(2020, 7, 1, 0, 25, 43),), 'passenger_count': 1, 'trip_distance': Decimal('9.50'), 'rate_code_id': 1, 'store_and_fwd_flag': 'N', 'pu_location_id': 138, 'do_location_id': 216, 'payment_type': '1', 'fare_amount': Decimal('26.5'), 'extra': Decimal('0.5'), 'mta_tax': Decimal('0.5'), 'tip_amount': Decimal('0'), 'tolls_amount': Decimal('0'), 'improvement_surcharge': Decimal('0.3'), 'total_amount': Decimal('27.8'), 'congestion_surcharge': Decimal('0')}
...
```

### AVRO
-

### Part 2
- run `docker volume create --name=hadoop-distributed-file-system` in bash

```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/docker/kafka
$ docker volume create --name=hadoop-distributed-file-system
hadoop-distributed-file-system
```

- run `docker volume ls` to check if it worked.

```bash

Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/docker/kafka
$ docker volume ls
DRIVER    VOLUME NAME
local     2a151c787da114b57fe0dded5adc9ca86724b6f71d41582222638272243cef6a
local     5a5f6809ddfac662a1a221f00afc6e296412cb1128a2edd48989eee74c396775
local     9de7a377924038dbd39e81e358b25cb0df5bd4fe7971493d872e8cb42cfaab54
local     51e58c8d0202d6d7a1eae5f50c596cd4d68e209c4d9f5e891f38803e0577ac6c
local     3595b4322dc57b3ec91afecec0b606fc15d51a398a3de9bcea671bbb046df4ce
local     b756cc1f3ee1961cd11ab5fa4f794482292aba46bcf6604bbae5bc57be5d55e9
local     c356096b3bdf9520db87ff08355c0a28e75ceb20b2f65e4f044d1d61f16c3057
local     c6859066070695087b050c24e53d277e39129a5143d7ff988f33d652c7ba31cb
local     d10b3bd362612e6e295eaecd633776b7ee98ff561d149a5883c1db62331a4a4f
local     dfca7e6b504482f8b3760ded13a74d632e417ad091da685c00dbba32cecbc737
local     e50d9e463d7c7f08e0d39997a8b141de05d1b51777cd8f90702182a43fe2b54e
local     hadoop-distributed-file-system
```

- run `./build.sh`
```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/docker/spark
$ ./build.sh
#0 building with "default" instance using docker driver

#1 [internal] load .dockerignore
#1 transferring context: 2B done
#1 DONE 0.4s

#2 [internal] load build definition from cluster-base.Dockerfile
#2 transferring dockerfile: 672B 0.0s done
#2 DONE 0.4s

#3 [internal] load metadata for docker.io/library/eclipse-temurin:17-jre
#3 DONE 2.5s

#4 [1/2] FROM docker.io/library/eclipse-temurin:17-jre@sha256:e61416273c1390e9d2850c084d6879554725bee3564bbe0ce280b826a6945222
#4 resolve docker.io/library/eclipse-temurin:17-jre@sha256:e61416273c1390e9d2850c084d6879554725bee3564bbe0ce280b826a6945222
#4 resolve docker.io/library/eclipse-temurin:17-jre@sha256:e61416273c1390e9d2850c084d6879554725bee3564bbe0ce280b826a6945222 0.2s done
#4 sha256:e61416273c1390e9d2850c084d6879554725bee3564bbe0ce280b826a6945222 1.70kB / 1.70kB done
#4 sha256:bfc1b60ae28d72a61d83b3ec69c115ecb0e23346171a23b8e812e3de2960e329 1.37kB / 1.37kB done
...
```

- run `docker compose up -d` in spark folder

```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/docker/spark
$ docker compose up -d
time="2024-03-02T18:43:03+01:00" level=warning msg="volume \"hadoop-distributed-file-system\" already exists but was not created by Docker Compose. Use `external: true` to use an existing volume"
 Container jupyterlab  Creating
 Container spark-master  Creating
 Container spark-master  Created
 Container spark-worker-2  Creating
 Container spark-worker-1  Creating
 Container jupyterlab  Created
 Container spark-worker-2  Created
 Container spark-worker-1  Created
 Container spark-master  Starting
 Container jupyterlab  Starting
 Container spark-master  Started
 Container spark-worker-1  Starting
 Container spark-worker-2  Starting
 Container jupyterlab  Started
 Container spark-worker-1  Started
 Container spark-worker-2  Started
```

- run `pip install pyspark`

```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/streams-example/pyspark
$ pip install pyspark
Collecting pyspark
  Using cached pyspark-3.5.1-py2.py3-none-any.whl
Collecting py4j==0.10.9.7
  Using cached py4j-0.10.9.7-py2.py3-none-any.whl (200 kB)
Installing collected packages: py4j, pyspark
Successfully installed py4j-0.10.9.7 pyspark-3.5.1
WARNING: You are using pip version 22.0.4; however, version 24.0 is available.
You should consider upgrading via the 'D:\DE-ZoomCamp\week_6_stream_python\python\env\Scripts\python.exe -m pip install --upgrade pip' command.
(env)
```

- run `python producer.py` in pyspark folder

```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/streams-example/pyspark
$ python producer.py
<zip object at 0x000001DD4487FC80>
Producing record for <key: 1, value:1, 2020-07-01 00:25:32, 2020-07-01 00:33:39, 1, 1.50, 2, 9.3>
Producing record for <key: 1, value:1, 2020-07-01 00:03:19, 2020-07-01 00:25:43, 1, 9.50, 1, 27.8>
Producing record for <key: 2, value:2, 2020-07-01 00:15:11, 2020-07-01 00:29:24, 1, 5.85, 2, 22.3>
Producing record for <key: 2, value:2, 2020-07-01 00:30:49, 2020-07-01 00:38:26, 1, 1.90, 1, 14.16>
Producing record for <key: 2, value:2, 2020-07-01 00:31:26, 2020-07-01 00:38:02, 1, 1.25, 2, 7.8>
(env)
```

- run ` python consumer.py`

```bash
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/streams-example/pyspark
$ python consumer.py
Consuming from Kafka started
Available topics to consume:  {'rides_csv'}
Key:1-type(<class 'int'>), Value:1, 2020-07-01 00:25:32, 2020-07-01 00:33:39, 1, 1.50, 2, 9.3-type(<class 'str'>)
Key:1-type(<class 'int'>), Value:1, 2020-07-01 00:03:19, 2020-07-01 00:25:43, 1, 9.50, 1, 27.8-type(<class 'str'>)
Key:2-type(<class 'int'>), Value:2, 2020-07-01 00:15:11, 2020-07-01 00:29:24, 1, 5.85, 2, 22.3-type(<class 'str'>)
Key:2-type(<class 'int'>), Value:2, 2020-07-01 00:30:49, 2020-07-01 00:38:26, 1, 1.90, 1, 14.16-type(<class 'str'>)
Key:2-type(<class 'int'>), Value:2, 2020-07-01 00:31:26, 2020-07-01 00:38:02, 1, 1.25, 2, 7.8-type(<class 'str'>)

(env)
```

- run `./spark-submit.sh streaming.py`

```bash 
Armut@Armut-PC MINGW64 /d/DE-ZoomCamp/week_6_stream_python/python/streams-example/pyspark
$ ./spark-submit.sh streaming.py
ps: unknown option -- o
Try `ps --help' for more information.
:: loading settings :: url = jar:file:/C:/tools/spark-3.5.0/jars/ivy-2.5.1.jar!/org/apache/ivy/core/settings/ivysettings.xml
Ivy Default Cache set to: C:\Users\Armut\.ivy2\cache
The jars for the packages stored in: C:\Users\Armut\.ivy2\jars
org.apache.spark#spark-sql-kafka-0-10_2.12 added as a dependency
org.apache.spark#spark-avro_2.12 added as a dependency
org.apache.spark#spark-streaming-kafka-0-10_2.12 added as a dependency
:: resolving dependencies :: org.apache.spark#spark-submit-parent-2a44431d-f5db-4f61-9a00-67800a3e85f8;1.0
        confs: [default]
        found org.apache.spark#spark-sql-kafka-0-10_2.12;3.3.1 in central
        found org.apache.spark#spark-token-provider-kafka-0-10_2.12;3.3.1 in central
        found org.apache.kafka#kafka-clients;2.8.1 in central
        found org.lz4#lz4-java;1.8.0 in central
        found org.xerial.snappy#snappy-java;1.1.8.4 in central
        found org.slf4j#slf4j-api;1.7.32 in central
        found org.apache.hadoop#hadoop-client-runtime;3.3.2 in central
...
```






