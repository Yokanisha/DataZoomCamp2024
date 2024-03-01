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

- go to your project file and type
- 
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
- Go to your producer.py file and run `python producer.py`
- Now, it should work.
- for deactivate run `deactivate`
- To activate it (you'll need to run it every time you need the virtual env): `./env/Scripts/activate`
