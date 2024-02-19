# Week 5: Batch Processing

## 5.1 Introduction

* :movie_camera: 5.1.1 Introduction to Batch Processing

BILD 022
BILD 023

- Batch Jobs
  - Weekly
  - Daily
  - Hourly
  - 3 times per hour
  - Every 5 minutes
 
- Technologies
  - Python scripts (Kubernetes, AWS Batch, ...)
  - SQL
  - Spark
  - Flink
 
BILD 024

- Advantages of Batch
  - Easy to manage
  - Retry
  - Scale

 - Disadvantage
   - Delay 
   - Higher Latency
   - Less Responsive

* :movie_camera: 5.1.2 Introduction to Spark

BILD 025
BILD 026
BILD 027



## 5.2 Installation

Follow [these intructions](setup/) to install Spark:

* [Windows](setup/windows.md)
* [Linux](setup/linux.md)
* [MacOS](setup/macos.md)

And follow [this](setup/pyspark.md) to run PySpark in Jupyter
-


* :movie_camera: 5.2.1 (Optional) Installing Spark (Linux)


-




## 5.3 Spark SQL and DataFrames

* :movie_camera: 5.3.1 First Look at Spark/PySpark

BILD 028
-

* :movie_camera: 5.3.2 Spark Dataframes

 Actions vs Transformation
- Transformations - lazy (not exectued immediately)
  -   Selecting columns
  -   Filtering
  -   ...
- Actions - eager (executed immediately)
  - Show, take, head
  - Write
 
  BILD 029

* :movie_camera: 5.3.3 (Optional) Preparing Yellow and Green Taxi Data

-

Script to prepare the Dataset [download_data.sh](code/download_data.sh)

> [!NOTE]  
> The other way to infer the schema (apart from pandas) for the csv files, is to set the `inferSchema` option to `true` while reading the files in Spark.

* :movie_camera: 5.3.4 SQL with Spark

-


## 5.4 Spark Internals

* :movie_camera: 5.4.1 Anatomy of a Spark Cluster

-

* :movie_camera: 5.4.2 GroupBy in Spark

-

* :movie_camera: 5.4.3 Joins in Spark

-

## 5.5 (Optional) Resilient Distributed Datasets

* :movie_camera: 5.5.1 Operations on Spark RDDs

-

* :movie_camera: 5.5.2 Spark RDD mapPartition

-


## 5.6 Running Spark in the Cloud

* :movie_camera: 5.6.1 Connecting to Google Cloud Storage


* :movie_camera: 5.6.2 Creating a Local Spark Cluster

-

* :movie_camera: 5.6.3 Setting up a Dataproc Cluster

-

* :movie_camera: 5.6.4 Connecting Spark to Big Query

-
