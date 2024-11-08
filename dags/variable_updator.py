from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


#lets define some of the default arguments which are not compulsory
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 8),
    'retries': 1,
}

def add_value(value, add_amount):
    return value + add_amount

def multiply_value(value, multiply_amount):
    return value * multiply_amount

def subtract_value(value, subtract_amount):
    return value - subtract_amount


# lets define the DAG
with DAG(
    'simple_variable_update_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Task A: Add a value to the variable
    task_add = PythonOperator(
        task_id='add_task',
        python_callable=add_value,
        op_args=[10, 5],  # Adds 5 to the initial value
        do_xcom_push=True,  # Push result to XCom
    )

    # Task B: Multiply the updated variable (get value from task_add using XCom)
    task_multiply = PythonOperator(
        task_id='multiply_task',
        python_callable=multiply_value,
        op_args=[task_add.output, 2],  # Get result from task_add and multiply by 2
        do_xcom_push = True
    
    )
    #Task C: subtract the updated variable 
    task_subtract = PythonOperator(
        task_id = "subtract_task",
        python_callable = subtract_value,
        op_args = [task_multiply.output, 10],
    )
    # lets define the  task dependencies using shift operators
    task_add >> task_multiply >> task_subtract
