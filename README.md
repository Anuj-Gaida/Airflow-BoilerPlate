# Airflow Boilerplate:
Apache Airflow is an open-source workflow orchestration tool that allows users to programmatically create, schedule, and monitor complex workflows. By defining workflows as Directed Acyclic Graphs (DAGs) in Python, Airflow makes it easy to manage dependencies between tasks and automate their execution. With a rich web interface for monitoring and logging, plus extensive integration options, Airflow is widely used for data engineering, ETL processes, and automating machine learning pipelines, helping teams streamline and scale their data workflows.

## Prerequisites
Airflow supports 3.6 or >3.6 python so make sure to update your python version 

## Installing Airflow:
## Step 1: Set up Airflow home directory
To set up the Airflow home directory, you need to define the location where Airflow will store its configuration files and data. This can be done by setting the AIRFLOW_HOME environment variable. In Windows, you would first set up a virtual environment using conda env or venv, and set the AIRFLOW_HOME environment variable there.
```bash
export AIRFLOW_HOME=~/airflow
```
Replace ~/airflow with the desired location for your Airflow home directory. This directory will be used to store logs, configuration files, and the Airflow SQLite database.

## Step 2: Install Apache Airflow

Only pip installation is currently officially supported:
```bash
pip install "apache-airflow[celery]==2.10.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.12.txt"
```
remember to change the constraints-3.12.txt version according to your system python version this is if python 3.7. , write 3.7.txt instead of 3.12.txt

## Step 3: Initilize backend
Before starting Airflow, you need to initialize the backend database. This can be done by running the following command:
```bash
airflow db init
```
This command will create the necessary tables and schemas in the Airflow SQLite database located in your AIRFLOW_HOME directory. If you plan to use a different database backend, such as MySQL or PostgreSQL, you will need to configure it accordingly.

## Step 4: Start the webserver
Once the backend is initialized, you can start the Airflow web server by running the following command:
```bash
airflow webserver -p 8080
```
This command will start the web server on port 8080, allowing you to access the Airflow user interface through your web browser. You can replace 8080 with the desired port number if needed. The webserver is a small API — it serves up the front-end and allows you, interacting with the front-end, to send it requests like starting an Airflow run or cancelling one.

