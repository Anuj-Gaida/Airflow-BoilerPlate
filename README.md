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

## For Simplicity and easier installation setting up Airflow in docker is higly recommended
First install docker and docker compose in your system
## Step 1: Fetch the compose file
For deploying Airflow on Docker Compose, you should fetch docker-compose.yaml.
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.3/docker-compose.yaml'
```

This configuration file defines multiple Airflow services:

- `airflow-scheduler`: Monitors all tasks and DAGs, triggering task instances after their dependencies are met.
- `airflow-webserver`: Accessible at http://localhost:8080, providing the Airflow UI.
- `airflow-worker`: Executes tasks as directed by the scheduler.
- `airflow-triggerer`: Runs event loops for deferrable tasks.
- `airflow-init`: Handles Airflow initialization.
- `postgres`: The database service.
- `redis`: Acts as a broker, relaying messages between the scheduler and worker.
Optionally, you can enable Flower for monitoring by using the --profile flower flag, which will make it available at http://localhost:5555.

These services together enable Airflow to run with CeleryExecutor. Key directories are synchronized between your computer and the container, including:

- `./dags` for DAG files
- `./logs` for task and scheduler logs
- `./config` for custom settings
- `./plugins` for custom plugins
  
The file uses the latest Airflow image (apache/airflow). To add Python or system libraries, you can build a custom image.

## Step 2: Initializing Environment
For first time, you need to prepare your environment, i.e. create the necessary files, directories and initialize the database.
# Setting up right airflow user
Before starting Airflow for the first time, you need to prepare your environment, i.e. create the necessary files, directories and initialize the database.
```bash
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
This will also create the .env file in your directory setting the AIRFLOW_UID=50000
something like this

## Step 3 : Now initialize the database
you need to run database migrations and create the first user account. Run the command:
```bash
docker compose up airflow-init
```
if you see the 
```bash
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.10.3
start_airflow-init_1 exited with code 0
```
on your terminal, congrats you have setup the user and databae
admin user is created with follwing credientials
```bash
username = airflow
password = airflow
```
## Step 4: Running the airflow
you can start all the serivce by:
```bash
docker compose up
```
## Step 4: Acessing through webserver
You can interact with Airflow in web ui is all your containers are up and healthy
it may take some time have patience
```bash
http://0.0.0.0:8080/home
```
![image](https://github.com/user-attachments/assets/9cff00db-e8ed-4c0d-a8f1-60d792cfb22d)

Congratulations you have sucessfully setup the docker for airflow..

## Now lets see the simple example of DAG I have created here
This is a simple dag that update a variable in 3 steps add, mul, sub. These steps are considered as 3 sequential task. I have attached the ss of DAG visualized from the web ui.
![image](https://github.com/user-attachments/assets/ef206d39-9153-4985-8d53-094d18153b9b)

## TO RUN MY CODE FOLLOW THE FOLLOWING STEP 
### Step 1: 
```bash
git clone git@github.com:Anuj-Gaida/Airflow-BoilerPlate.git
```
### Step 2:
```bash
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
### Step 3:
```bash
docker compose airflow-init
docker compose up
```

**Note**
I have replace CeleryExecuter by Local executer 
![image](https://github.com/user-attachments/assets/27c8f7ba-c7d4-4964-8c68-714474e21028)
And replaced redis and flower services, you can also modify the compose file according to your needs and ease


