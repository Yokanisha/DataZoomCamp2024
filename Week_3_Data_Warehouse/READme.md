# Data Warehouse and BigQuery

- [Slides](https://docs.google.com/presentation/d/1a3ZoBAXFk8-EhUsd7rAZd-5p_HpltkzSeujjRGB2TAI/edit?usp=sharing)  
- [Big Query basic SQL](big_query.sql)

# Videos

## Data Warehouse

- [Data Warehouse and BigQuery](https://www.youtube.com/watch?v=jrHljAoD6nM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

### OLTP & OLAP
|   | OLTP | OLAP |
|---|---|---|
| Purpose | Control and run essential business operations in real time | Plan, solve problems, support decisions, discover hidden insights |
| Data updates | Short, fast updates initiated by user | Data periodically refreshed with scheduled, long-running batch jobs |
| Database design | Normalized databases for efficiency | Denormalized databases for analysis |
| Space requirements | Generally small if historical data is archived | Generally large due to aggregating large datasets |
| Backup and recovery | Regular backups required to ensure business continuity and meet legal and governance requirements | Lost data can be reloaded from OLTP database as needed in lieu of regular backups |
| Productivity | Increases productivity of end users | Increases productivity of business managers, data analysts and executives |
| Data view | Lists day-to-day business transactions | Multi-dimensional view of enterprise data |
| User examples | Customer-facing personnel, clerks, online shoppers | Knowledge workers such as data analysts, business analysts and executives |

### BigQuery

BigQuery is a fully-managed, serverless cloud data warehouse provided by Google Cloud. It enables organizations to analyze and query large datasets in real-time using SQL-like queries. BigQuery is designed for high-performance and scalability, allowing users to process massive amounts of data quickly and cost-effectively. It supports both real-time data streaming and batch processing, making it a powerful tool for analytics, business intelligence, and data exploration in a cloud environment.

- Serverless data warehouse
  - There are no servers to manage or database software to install
- Software as well as infrastructure including
  - **scalability** and **high-availability**
- Built-in features like
  - machine learning
  - geospatial analysis
  - business intelligence
- BigQuery maximizes flexibility by separating the compute engine that analyzes your data from your storage
- On demand pricing
  - 1 TB of data processed is \$5
- Flat rate pricing
  - Based on number of pre requested slots
  - 100 slots → \$2,000/month = 400 TB data processed on demand pricing
 


### Data Warehouse

A Data Warehouse (DW) is designed as an Online Analytical Processing (OLAP) solution primarily for reporting and data analysis. In contrast to Data Lakes, which adhere to the Extract, Load, Transform (ELT) model, Data Warehouses commonly employ the Extract, Transform, Load (ETL) model, as explained in lesson 2.

In the ETL process, a Data Warehouse gathers data from various sources, undergoes processing in a staging area, and is then loaded into the actual warehouse, typically a database, where it is organized according to requirements. Data Warehouses may also distribute data to separate Data Marts, which are smaller database systems that end users can utilize for specific purposes.

![OLAP solution](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/004.PNG)

## BigQuery queries
```sql
-- Query public available table
SELECT station_id, name FROM
    bigquery-public-data.new_york_citibike.citibike_stations
LIMIT 100;
```

```sql
-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `taxi-rides-ny.nytaxi.external_yellow_tripdata`
OPTIONS (
  format = 'CSV',
  uris = ['gs://nyc-tl-data/trip data/yellow_tripdata_2019-*.csv', 'gs://nyc-tl-data/trip data/yellow_tripdata_2020-*.csv']
);
```

```sql
-- Check yello trip data
SELECT * FROM taxi-rides-ny.nytaxi.external_yellow_tripdata limit 10;
```

```sql
-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_non_partitoned AS
SELECT * FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;
```

```sql
-- Create a partitioned table from external table
CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_partitoned
PARTITION BY
  DATE(tpep_pickup_datetime) AS
SELECT * FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;
```

```sql
-- Impact of partition
-- Scanning 1.6GB of data
SELECT DISTINCT(VendorID)
FROM taxi-rides-ny.nytaxi.yellow_tripdata_non_partitoned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2019-06-30';
```

```sql
-- Scanning ~106 MB of DATA
SELECT DISTINCT(VendorID)
FROM taxi-rides-ny.nytaxi.yellow_tripdata_partitoned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2019-06-30';
```

```sql
-- Let's look into the partitons
SELECT table_name, partition_id, total_rows
FROM `nytaxi.INFORMATION_SCHEMA.PARTITIONS`
WHERE table_name = 'yellow_tripdata_partitoned'
ORDER BY total_rows DESC;
```

```sql
-- Creating a partition and cluster table
CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_partitoned_clustered
PARTITION BY DATE(tpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;
```

```sql
-- Query scans 1.1 GB
SELECT count(*) as trips
FROM taxi-rides-ny.nytaxi.yellow_tripdata_partitoned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
  AND VendorID=1;
```

```sql
-- Query scans 864.5 MB
SELECT count(*) as trips
FROM taxi-rides-ny.nytaxi.yellow_tripdata_partitoned_clustered
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
  AND VendorID=1;
```


## :movie_camera: Partitoning and clustering

- [Partioning and Clustering](https://www.youtube.com/watch?v=jrHljAoD6nM&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)  
- [Partioning vs Clustering](https://www.youtube.com/watch?v=-CqXf7vhhDs&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

### Partitioning
![BigQuery Partitioning](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/005.PNG)

BigQuery partition
- Time-unit column
- Ingestion time (_PARTITIONTIME)
- Integer range partitioning
- When using Time unit or ingestion time
  - Daily (Default)
  - Hourly
  - Monthly or yearly
- Number of partitions limit is 4000
- Resource: https://cloud.google.com/bigquery/docs/partitioned-tables

BigQuery Clustering
- Columns you specify are used to colocate related data
- Order of the column is important
- The order of the specified columns determines the sort order of the data.
- Clustering improves
  - Filter queries
  - Aggregate queries
- Table with data size < 1 GB, don’t show significant improvement with partitioning and clustering
- You can specify up to four clustering columns

- Clustering columns must be top-level, non-repeated columns
  - DATE
  - BOOL
  - GEOGRAPHY
  - INT64
  - NUMERIC
  - BIGNUMERIC
  - STRING
  - TIMESTAMP
  - DATETIME




### Partitioning & Clustering
![BigQuery Partitioning & Clustering](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/006.PNG)


### Partitioning vs CLustering
|  CLustering | Partitioning |
|---|---|
| Cost benefit unknown | Cost known upfront |
| You need more granularity than partitioning alone allows | You need partition-level management |
| Your queries commonly use filters or aggregation against multiple particular columns| Filter or aggregate on single column |
| The cardinality of the number of values in a column or group of columns is large | Generally small if historical data is archived |

### Clustering over paritioning
- Partitioning results in a small amount of data per partition (approximately less than 1 GB)
- Partitioning results in a large number of partitions beyond the limits on partitioned tables
- Partitioning results in your mutation operations modifying the majority of partitions in the table frequently (for example, every few minutes)

### Automatic reclustering
- As data is added to a clustered table
  - the newly inserted data can be written to blocks that contain key ranges that overlap with the key ranges in previously written blocks
  - These overlapping keys weaken the sort property of the table
- To maintain the performance characteristics of a clustered table
  - BigQuery performs automatic re-clustering in the background to restore the sort property of the table
  - For partitioned tables, clustering is maintained for data within the scope of each partition.


## :movie_camera: Best practices

- [BigQuery Best Practices](https://www.youtube.com/watch?v=k81mLJVX08w&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

- Cost reduction
  - Avoid SELECT *
  - Price your queries before running them
  - Use clustered or partitioned tables
  - Use streaming inserts with caution
  - Materialize query results in stages
- Query performance
  - Filter on partitioned columns
  - Denormalizing data
  - Use nested or repeated columns
  - Use external data sources appropriately
  - Don't use it, in case u want a high query performance
  - Reduce data before using a JOIN
  - Do not treat WITH clauses as prepared statements
  - Avoid oversharding tables
- Query performance
  - Avoid JavaScript user-defined functions
  - Use approximate aggregation functions (HyperLogLog++)
  - Order Last, for query operations to maximize performance
  - Optimize your join patterns
    - As a best practice, place the table with the largest number of rows first, followed by the table with the fewest rows, and then place the remaining tables by decreasing size.


BigQuery relies on four key infrastructure technologies:

- ***Dremel***: This component handles the computation aspect of BigQuery by executing SQL queries. It transforms SQL queries into execution trees, where the leaves are referred to as "slots" responsible for reading data from storage and performing calculations. The branches, known as "mixers," handle aggregation. Dremel dynamically allocates slots to queries while ensuring fairness for concurrent queries from multiple users.
- ***Colossus***: Google's global storage system is leveraged by BigQuery. It employs a columnar storage format and compression algorithms for efficient data storage. Colossus is optimized for reading large volumes of structured data and manages tasks such as replication, recovery, and distributed management.
- ***Jupiter***: This is the network that facilitates communication between Dremel and Colossus. Jupiter is an in-house network technology developed by Google for interconnecting its data centers.
- ***Borg***: Serving as an orchestration solution, Borg handles various aspects of the infrastructure. It is a precursor to Kubernetes, managing tasks related to the coordination and deployment of services within the BigQuery ecosystem.


![infrastructure](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/007.PNG)


### Record-oriented vs column-oriented storage
Traditional methods for storing tabular data are record-oriented, also known as row-oriented. Data is read sequentially, row by row, and then the columns are accessed per row. An example of this is a CSV file, where each new line in the file represents a record, and all the information for that specific record is contained within that line.

BigQuery, on the other hand, utilizes a columnar storage format. Data is stored based on the columns of the table rather than the rows. This approach proves beneficial when dealing with massive amounts of data because it allows us to immediately discard columns not of interest when performing queries, thereby reducing the amount of processed data.

![Record and column](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/008.PNG)

During the query execution process, Dremel transforms queries to construct an execution tree. Different parts of the query are assigned to various mixers, each of which further delegates smaller segments to different slots. These slots access Colossus to retrieve the required data.

The choice of a columnar storage format proves ideal for this workflow. It enables rapid data retrieval from Colossus by multiple workers. These workers then conduct necessary computations on the retrieved datapoints, returning the results to the mixers. The mixers perform any required aggregations before sending the data back to the root server. Finally, the root server compiles the final output of the query.

![more](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/009.PNG)


## Reference
- [How does BigQuery work?](https://cloud.google.com/bigquery/docs/storage_overview)
- [Dremel: Interactive Analysis of Web-Scale Datasets](https://research.google/pubs/dremel-interactive-analysis-of-web-scale-datasets-2/)
- [A Deep Dive Into Google BigQuery Architecture: How It Works](https://panoply.io/data-warehouse-guide/bigquery-architecture/)
- [A look at Dremel](https://www.goldsborough.me/distributed-systems/2019/05/18/21-09-00-a_look_at_dremel/)

## :movie_camera: Internals of BigQuery

- [Internals of Big Query](https://www.youtube.com/watch?v=eduHi1inM4s&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

## Advanced topics

### :movie_camera: Machine Learning in Big Query

* [BigQuery Machine Learning](https://www.youtube.com/watch?v=B-WtpB0PuG4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
* [SQL for ML in BigQuery](big_query_ml.sql)

***ML in BigQuery***
- Target audience Data analysts, managers
- No need for Python or Java knowledge
- No need to export data into a different system


***ML in BigQuery pricing (Free)***
- 10 GB per month of data storage
- 1 TB per month of queries processed
- ML Create model step: First 10 GB per month is free

![Pricing](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/010.PNG)

### Introduction to BigQuery ML
BigQuery ML lets you create and run machine learning (ML) models by using GoogleSQL queries. It also lets you access LLMs and Cloud AI APIs to perform artificial intelligence (AI) tasks like text generation or machine translation.

Usually, performing ML or AI on large datasets requires extensive programming and knowledge of ML frameworks. These requirements restrict solution development to a very small set of people within each company, and they exclude data analysts who understand the data but have limited ML knowledge and programming expertise. However, with BigQuery ML, SQL practitioners can use existing SQL tools and skills to build and evaluate models, and to generate results from LLMs and Cloud AI APIs.
![more](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/011.PNG)

[Introduction to BigQuery ML](https://cloud.google.com/bigquery/docs/bqml-introduction#model_selection_guide)

***Model selection guide***

![more](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/012.PNG)

[Model selection guide](https://cloud.google.com/bigquery/docs/bqml-introduction#model_selection_guide)

### BigQuery ML queries

```sql
-- SELECT THE COLUMNS INTERESTED FOR YOU
SELECT passenger_count, trip_distance, PULocationID, DOLocationID, payment_type, fare_amount, tolls_amount, tip_amount
FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitoned` WHERE fare_amount != 0;
```

```sql
-- CREATE A ML TABLE WITH APPROPRIATE TYPE
CREATE OR REPLACE TABLE `taxi-rides-ny.nytaxi.yellow_tripdata_ml` (
`passenger_count` INTEGER,
`trip_distance` FLOAT64,
`PULocationID` STRING,
`DOLocationID` STRING,
`payment_type` STRING,
`fare_amount` FLOAT64,
`tolls_amount` FLOAT64,
`tip_amount` FLOAT64
) AS (
SELECT passenger_count, trip_distance, cast(PULocationID AS STRING), CAST(DOLocationID AS STRING),
CAST(payment_type AS STRING), fare_amount, tolls_amount, tip_amount
FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitoned` WHERE fare_amount != 0
);
```

```sql
-- CREATE MODEL WITH DEFAULT SETTING
CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_model`
OPTIONS
(model_type='linear_reg',
input_label_cols=['tip_amount'],
DATA_SPLIT_METHOD='AUTO_SPLIT') AS
SELECT
*
FROM
`taxi-rides-ny.nytaxi.yellow_tripdata_ml`
WHERE
tip_amount IS NOT NULL;
```

```sql
-- CHECK FEATURES
SELECT * FROM ML.FEATURE_INFO(MODEL `taxi-rides-ny.nytaxi.tip_model`);
```

```sql
-- EVALUATE THE MODEL
SELECT
*
FROM
ML.EVALUATE(MODEL `taxi-rides-ny.nytaxi.tip_model`,
(
SELECT
*
FROM
`taxi-rides-ny.nytaxi.yellow_tripdata_ml`
WHERE
tip_amount IS NOT NULL
));
```

```sql
-- PREDICT THE MODEL
SELECT
*
FROM
ML.PREDICT(MODEL `taxi-rides-ny.nytaxi.tip_model`,
(
SELECT
*
FROM
`taxi-rides-ny.nytaxi.yellow_tripdata_ml`
WHERE
tip_amount IS NOT NULL
));
```

```sql
-- PREDICT AND EXPLAIN
SELECT
*
FROM
ML.EXPLAIN_PREDICT(MODEL `taxi-rides-ny.nytaxi.tip_model`,
(
SELECT
*
FROM
`taxi-rides-ny.nytaxi.yellow_tripdata_ml`
WHERE
tip_amount IS NOT NULL
), STRUCT(3 as top_k_features));
```

```sql
-- HYPER PARAM TUNNING
CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_hyperparam_model`
OPTIONS
(model_type='linear_reg',
input_label_cols=['tip_amount'],
DATA_SPLIT_METHOD='AUTO_SPLIT',
num_trials=5,
max_parallel_trials=2,
l1_reg=hparam_range(0, 20),
l2_reg=hparam_candidates([0, 0.1, 1, 10])) AS
SELECT
*
FROM
`taxi-rides-ny.nytaxi.yellow_tripdata_ml`
WHERE
tip_amount IS NOT NULL;
```




**Important links**

- [BigQuery ML Tutorials](https://cloud.google.com/bigquery-ml/docs/tutorials)
- [BigQuery ML Reference Parameter](https://cloud.google.com/bigquery-ml/docs/analytics-reference-patterns)
- [Hyper Parameter tuning](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-glm)
- [Feature preprocessing](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-preprocess-overview)

### :movie_camera: Deploying ML model

- [BigQuery Machine Learning Deployment](https://www.youtube.com/watch?v=BjARzEWaznU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
- [Steps to extract and deploy model with docker](extract_model.md)  



# Homework

* [2024 Homework](../cohorts/2024/03-data-warehouse/homework.md)
