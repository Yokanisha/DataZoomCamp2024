## 📕 Course Resources

### 2.2.1 - 📯 Intro to Orchestration

In this section, we'll cover the basics of workflow orchestration. We'll discuss what it is, why it's important, and how it can be used to build data pipelines.

Notes
-
-
-



### 2.2.2 - 🧙‍♂️ Intro to Mage

In this section, we'll introduce the Mage platform. We'll cover what makes Mage different from other orchestrators, the fundamental concepts behind Mage, and how to get started. To cap it off, we'll spin Mage up via Docker 🐳 and run a simple pipeline.

Notes
-
-
-

### 2.2.3 - 🐘 ETL: API to Postgres

Hooray! Mage is up and running. Now, let's build a _real_ pipeline. In this section, we'll build a simple ETL pipeline that loads data from an API into a Postgres database. Our database will be built using Docker— it will be running locally, but it's the same as if it were running in the cloud.

Notes
-
-
-


### 2.2.4 - 🤓 ETL: API to GCS

Ok, so we've written data _locally_ to a database, but what about the cloud? In this tutorial, we'll walk through the process of using Mage to extract, transform, and load data from an API to Google Cloud Storage (GCS). 

We'll cover both writing _partitioned_ and _unpartitioned_ data to GCS and discuss _why_ you might want to do one over the other. Many data teams start with extracting data from a source and writing it to a data lake _before_ loading it to a structured data source, like a database.

Notes
-
-
-

### 2.2.5 - 🔍 ETL: GCS to BigQuery

Now that we've written data to GCS, let's load it into BigQuery. In this section, we'll walk through the process of using Mage to load our data from GCS to BigQuery. This closely mirrors a very common data engineering workflow: loading data from a data lake into a data warehouse.

Notes
-
-
-

### 2.2.6 - 👨‍💻 Parameterized Execution

By now you're familiar with building pipelines, but what about adding parameters? In this video, we'll discuss some built-in runtime variables that exist in Mage and show you how to define your own! We'll also cover how to use these variables to parameterize your pipelines. Finally, we'll talk about what it means to *backfill* a pipeline and how to do it in Mage.

Notes
-
-
-

### 2.2.7 - 🤖 Deployment (Optional)

In this section, we'll cover deploying Mage using Terraform and Google Cloud. This section is optional— it's not *necessary* to learn Mage, but it might be helpful if you're interested in creating a fully deployed project. If you're using Mage in your final project, you'll need to deploy it to the cloud.

Notes
-
-
-

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
