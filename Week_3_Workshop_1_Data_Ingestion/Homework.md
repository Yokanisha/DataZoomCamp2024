# Data ingestion with dlt

​In this hands-on workshop, we’ll learn how to build data ingestion pipelines.

​We’ll cover the following steps:

* ​Extracting data from APIs, or files.
* ​Normalizing and loading data
* ​Incremental loading

​By the end of this workshop, you’ll be able to write data pipelines like a senior data engineer: Quickly, concisely, scalable, and self-maintaining.



--- 

# Navigation

* [Workshop content](dlt_resources/data_ingestion_workshop.md)
* [Workshop notebook](dlt_resources/workshop.ipynb)
* [Homework starter notebook](dlt_resources/homework_starter.ipynb)

# Resources

- Website and community: Visit our [docs](https://dlthub.com/docs/intro), discuss on our slack (Link at top of docs).
- Course colab: [Notebook](https://colab.research.google.com/drive/1kLyD3AL-tYf_HqCXYnA3ZLwHGpzbLmoj#scrollTo=5aPjk0O3S_Ag&forceEdit=true&sandboxMode=true).
- dlthub [community Slack](https://dlthub.com/community).

---


# Course
You can find the course file [here](./dlt_resources/data_ingestion_workshop.md)
The course has 3 parts
- [Extraction Section](./dlt_resources/data_ingestion_workshop.md#extracting-data): In this section we will learn about scalable extraction
- [Normalisation Section](./dlt_resources/data_ingestion_workshop.md#normalisation): In this section we will learn to prepare data for loading
- [Loading Section](./dlt_resources/data_ingestion_workshop.md#incremental-loading)): Here we will learn about incremental loading modes

---

# Homework

The [linked colab notebook](https://colab.research.google.com/drive/1Te-AT0lfh0GpChg1Rbd0ByEKOHYtWXfm#scrollTo=wLF4iXf-NR7t&forceEdit=true&sandboxMode=true) offers a few exercises to practice what you learned today.


#### Question 1: What is the sum of the outputs of the generator for limit = 5?
- **A**: 10.23433234744176
- **B**: 7.892332347441762
- **C**: 8.382332347441762 👍
- **D**: 9.123332347441762

```python
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 5
generator = square_root_generator(limit)
sum = 0
for sqrt_value in generator:
    print(sqrt_value)
    sum += sqrt_value

print("sum: ", sum)
```

```
1.0
1.4142135623730951
1.7320508075688772
2.0
2.23606797749979
sum:  8.382332347441762
```

#### Question 2: What is the 13th number yielded by the generator?
- **A**: 4.236551275463989
- **B**: 3.605551275463989 👍
- **C**: 2.345551275463989
- **D**: 5.678551275463989

```python
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 13
generator = square_root_generator(limit)

for i, sqrt_value in enumerate(generator):
    print(i+1, ":", sqrt_value)
```

```
1 : 1.0
2 : 1.4142135623730951
3 : 1.7320508075688772
4 : 2.0
5 : 2.23606797749979
6 : 2.449489742783178
7 : 2.6457513110645907
8 : 2.8284271247461903
9 : 3.0
10 : 3.1622776601683795
11 : 3.3166247903554
12 : 3.4641016151377544
13 : 3.605551275463989
```

#### Question 3: Append the 2 generators. After correctly appending the data, calculate the sum of all ages of people.
- **A**: 353 👍
- **B**: 365
- **C**: 378
- **D**: 390

```python
import dlt

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

for person in people_1():
    print(person)

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

for person in people_2():
    print(person)

generators_pipeline = dlt.pipeline(destination='duckdb', dataset_name='generators')

info = generators_pipeline.run(people_1(), table_name="people")

print(info)

info = generators_pipeline.run(people_2(),table_name="people")

print(info)
```

```python
import duckdb

conn = duckdb.connect(f"{generators_pipeline.pipeline_name}.duckdb")

conn.sql(f"SET search_path = '{generators_pipeline.dataset_name}'")
print('Loaded tables: ')
display(conn.sql("show tables"))

print("\n\n\n people table below:")
rides = conn.sql("SELECT sum(age) FROM people").df()
display(rides)
```
#### Question 4: Merge the 2 generators using the ID column. Calculate the sum of ages of all the people loaded as described above.
- **A**: 205
- **B**: 213
- **C**: 221
- **D**: 230

- E: I have the number 266

```python
import dlt

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

for person in people_1():
    print(person)


def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


for person in people_2():
    print(person)

generators_pipeline = dlt.pipeline(destination='duckdb', dataset_name='generators')

info = generators_pipeline.run(people_1(), table_name="people_merge", write_disposition="merge", primary_key="ID")

print(info)

info = generators_pipeline.run(people_2(), table_name="people_merge", write_disposition="merge", primary_key="ID")

print(info)
```

```python
import duckdb

conn = duckdb.connect(f"{generators_pipeline.pipeline_name}.duckdb")

conn.sql(f"SET search_path = '{generators_pipeline.dataset_name}'")
print('Loaded tables: ')
display(conn.sql("show tables"))

print("\n\n\n people table below:")
rides = conn.sql("SELECT * FROM people_merge").df()
display(rides)
```

Submit the solution here: https://courses.datatalks.club/de-zoomcamp-2024/homework/workshop1

--- 
# Next steps

As you are learning the various concepts of data engineering, 
consider creating a portfolio project that will further your own knowledge.

By demonstrating the ability to deliver end to end, you will have an easier time finding your first role. 
This will help regardless of whether your hiring manager reviews your project, largely because you will have a better 
understanding and will be able to talk the talk.

Here are some example projects that others did with dlt:
- Serverless dlt-dbt on cloud functions: [Article](https://docs.getdbt.com/blog/serverless-dlt-dbt-stack)
- Bird finder: [Part 1](https://publish.obsidian.md/lough-on-data/blogs/bird-finder-via-dlt-i), [Part 2](https://publish.obsidian.md/lough-on-data/blogs/bird-finder-via-dlt-ii)
- Event ingestion on GCP: [Article and repo](https://dlthub.com/docs/blog/streaming-pubsub-json-gcp)
- Event ingestion on AWS: [Article and repo](https://dlthub.com/docs/blog/dlt-aws-taktile-blog)
- Or see one of the many demos created by our working students: [Hacker news](https://dlthub.com/docs/blog/hacker-news-gpt-4-dashboard-demo), 
[GA4 events](https://dlthub.com/docs/blog/ga4-internal-dashboard-demo), 
[an E-Commerce](https://dlthub.com/docs/blog/postgresql-bigquery-metabase-demo), 
[google sheets](https://dlthub.com/docs/blog/google-sheets-to-data-warehouse-pipeline), 
[Motherduck](https://dlthub.com/docs/blog/dlt-motherduck-demo), 
[MongoDB + Holistics](https://dlthub.com/docs/blog/MongoDB-dlt-Holistics), 
[Deepnote](https://dlthub.com/docs/blog/deepnote-women-wellness-violence-tends), 
[Prefect](https://dlthub.com/docs/blog/dlt-prefect),
[PowerBI vs GoodData vs Metabase](https://dlthub.com/docs/blog/semantic-modeling-tools-comparison),
[Dagster](https://dlthub.com/docs/blog/dlt-dagster),
[Ingesting events via gcp webhooks](https://dlthub.com/docs/blog/dlt-webhooks-on-cloud-functions-for-event-capture),
[SAP to snowflake replication](https://dlthub.com/docs/blog/sap-hana-to-snowflake-demo-blog),
[Read emails and send sumamry to slack with AI and Kestra](https://dlthub.com/docs/blog/dlt-kestra-demo-blog),
[Mode +dlt capabilities](https://dlthub.com/docs/blog/dlt-mode-blog),
[dbt on cloud functions](https://dlthub.com/docs/blog/dlt-dbt-runner-on-cloud-functions)
- If you want to use dlt in your project, [check this list of public APIs](https://dlthub.com/docs/blog/practice-api-sources)


If you create a personal project, consider submitting it to our blog - we will be happy to showcase it. Just drop us a line in the dlt slack.



**And don't forget, if you like dlt**
- **Give us a [GitHub Star!](https://github.com/dlt-hub/dlt)**
- **Join our [Slack community](https://dlthub.com/community)**


# Notes

* Add your notes here
