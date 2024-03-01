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



