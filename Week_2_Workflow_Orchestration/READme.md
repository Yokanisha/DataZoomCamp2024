## 📕 Course Resources

### 2.2.1 - 📯 Intro to Orchestration

In this section, we'll cover the basics of workflow orchestration. We'll discuss what it is, why it's important, and how it can be used to build data pipelines.

### Notes
- https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/001.PNG

### Architecture
#### Extract
- Pull data from a source (API - NYC taxi dataset)
#### Transform
- Data clkeaning, transformation and partitioning
#### Load
- API to Mage, Mage to Postgres, GCS, BigQuery

  
![What we wanna do](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/001.PNG)

#### What is Orchestration?
- A large part of data engineering is extracting, transforming, and loading data between sources.
- Orchestration is a process of dependency management, facilitated through automation. 
- The data orchestrator manages scheduling, triggering, monitoring, and even resource allocation. 

#### A good orchestrator handles…
- Workflow management
- Automation
- Error handling 
- Recovery
- Monitoring, alerting
- Resource optimization
- Observability
- Debugging
- Compliance/Auditing

#### A good orchestrator prioritizes….
The developer experience
- Flow state 🌊
  “I need to switch between 7 tools/services.”
- Feedback Loops 🔁
  “I spent 5 hours locally testing this DAG.”
- Cognitive Load 🧱
  How much do you need to know to do your job?



### 2.2.2 - 🧙‍♂️ Intro to Mage

In this section, we'll introduce the Mage platform. We'll cover what makes Mage different from other orchestrators, the fundamental concepts behind Mage, and how to get started. To cap it off, we'll spin Mage up via Docker 🐳 and run a simple pipeline.

### Notes
#### What is Mage?
- An open-source pipeline tool for orchestrating, transforming, and integrating data
![What is Mage?](https://github.com/Yokanisha/DataZoomCamp2024/blob/main/Images/002.PNG)

#### 👨🏻‍💻 Engineering best-practices built-in 
- 🧪 In-line testing and debugging
  - Familiar, notebook-style format
- 🔎 Fully-featured observability
  - Transformation in one place: dbt models, streaming, & more.
- 🏜️ DRY principles
  - No more 🍝 DAGs with duplicate functions and weird imports
  - DEaaS (sorry, I had to 😅)

#### 🏗️ Projects
- A project forms the basis for all the work you can do in Mage— you can think of it like a GitHub repo. 
- It contains the code for all of your pipelines, blocks, and other assets.
- A Mage instance has one or more projects

#### 🧪 Pipelines

- A pipeline is a workflow that executes some data operation— maybe extracting, transforming, and loading data from an API. They’re also called DAGs on other platforms
- In Mage, pipelines can contain Blocks (written in SQL, Python, or R) and charts. 
- Each pipeline is represented by a YAML file in the “pipelines” folder of your project.

#### 🧱 Blocks
- A block is a file that can be executed independently or within a pipeline. 
- Together, blocks form Directed Acyclic Graphs (DAGs), which we call pipelines. 
- A block won’t start running in a pipeline until all its upstream dependencies are met.
- Blocks are reusable, atomic pieces of code that perform certain actions. 
- Changing one block will change it everywhere it’s used, but don’t worry, it’s easy to detach blocks to separate instances if necessary.
- Blocks can be used to perform a variety of actions, from simple data transformations to complex machine learning models.

### Configure mage
- git clone https://github.com/mage-ai/mage-zoomcamp.git mage-zoomcamp
- cd mage-zoomcamp
- ls -la
- cp dev.env .env
- winpty docker-compose build
- docker pull mageai/mageai:latest
- winpty docker-compose up
Now, navigate to http://localhost:6789 in your browser!


### 2.2.3 - 🐘 ETL: API to Postgres

Hooray! Mage is up and running. Now, let's build a _real_ pipeline. In this section, we'll build a simple ETL pipeline that loads data from an API into a Postgres database. Our database will be built using Docker— it will be running locally, but it's the same as if it were running in the cloud.

### Notes
- We have learned the `ETL`-process in this course.


### 2.2.4 - 🤓 ETL: API to GCS

Ok, so we've written data _locally_ to a database, but what about the cloud? In this tutorial, we'll walk through the process of using Mage to extract, transform, and load data from an API to Google Cloud Storage (GCS). 

We'll cover both writing _partitioned_ and _unpartitioned_ data to GCS and discuss _why_ you might want to do one over the other. Many data teams start with extracting data from a source and writing it to a data lake _before_ loading it to a structured data source, like a database.

#### Configuring GCP
- create a bucket (google cloud storage) # I choosed the name `mage-zoomcamp-matt-palmer-1`
- create a service account (IAM & ADMIN -> create service account) # I choosed the name `mage-zoomcamp`
  - Role -> basics -> owner -> continue
  - Choose in the register 'KEYS' and create a new Key (JSON) -> Save it into the mage project
- Go to mage -> File -> io_config.yaml
    - Go to `#Google` ->  Delete all under 'Google' except these two and fill the correct path to your json-key-file and location which you choosed when you created you bucket (under `Choose where to store your data`)
 
```mage
  GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/evident-beacon-XXXX-YYYYY.json"
  GOOGLE_LOCATION: EU # Optional
```

- Go to mage -> test_config -> create a SQL-Loader (BigQuery and default) -> 'SELECT 1; -> does it work? -> yes? -> good! :) You can delete it
- Go to GCP to your bucket -> put  your `titanic_clean.csv` in it.
- Go to mage -> Create a data loader (SQL -> Python -> Google Cloud Storage)
    - change `bucket_name` and `object_key`

```SQL
@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    ...
    bucket_name = 'mage-zoomcamp-matt-palmer-1'
    object_key = 'titanic_clean.csv'
    ...
```
- run and see if it works.


#### ETL: API to GCP
We learned
- How to `extract` data from an URL path in mage
- How to `transform` the data in mage
- How to `load` the data in gcp 


### 2.2.5 - 🔍 ETL: GCS to BigQuery

Now that we've written data to GCS, let's load it into BigQuery. In this section, we'll walk through the process of using Mage to load our data from GCS to BigQuery. This closely mirrors a very common data engineering workflow: loading data from a data lake into a data warehouse.

We learned
- How to `extract` data from an gcp bucket
- How to `transform` the data in mage
- How to `load` the data in BigQuery 


### 2.2.6 - 👨‍💻 Parameterized Execution

By now you're familiar with building pipelines, but what about adding parameters? In this video, we'll discuss some built-in runtime variables that exist in Mage and show you how to define your own! We'll also cover how to use these variables to parameterize your pipelines. Finally, we'll talk about what it means to *backfill* a pipeline and how to do it in Mage.

Notes
- [Mage Variables Overview](https://docs.mage.ai/development/variables/overview)
- [Mage Runtime Variables](https://docs.mage.ai/getting-started/runtime-variable)

### 2.2.7 - 🤖 Deployment (Optional)

In this section, we'll cover deploying Mage using Terraform and Google Cloud. This section is optional— it's not *necessary* to learn Mage, but it might be helpful if you're interested in creating a fully deployed project. If you're using Mage in your final project, you'll need to deploy it to the cloud.

Notes


#### Prerequisit
- Terraform
- gcloud cli
- Google Cloud Permissions
- Mage Terraform templates

#### Permissions we need
- Go to `IAM` in Google Cloud and eddit your project
- Assign roles which you only need:
  - Owner
  - Artifact Registry Reader
  - Artifact Registry Writer
  - Cloud Run developer
  - Cloud SQL Admin
  - Service Account Token Creator
 
#### Deploying to Google Cloud
- We need it for our final Porject!
- make sure to install and config Terraform first!


### 2.2.8 - 🗒️ Homework 

We've prepared a short exercise to test you on what you've learned this week. You can find the homework [here](../cohorts/2024/02-workflow-orchestration/homework.md). This follows closely from the contents of the course and shouldn't take more than an hour or two to complete. 😄

### 2.2.9 - 👣 Next Steps

Congratulations! You've completed Week 2 of the Data Engineering Zoomcamp. We hope you've enjoyed learning about Mage and that you're excited to use it in your final project. If you have any questions, feel free to reach out to us on Slack. Be sure to check out our "Next Steps" video for some inspiration for the rest of your journey 😄.

Notes
-
-
-

### 📑 Additional Resources

- [Mage Docs](https://docs.mage.ai/)
- [Mage Guides](https://docs.mage.ai/guides)
- [Mage Slack](https://www.mage.ai/chat)
