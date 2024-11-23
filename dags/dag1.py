from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define a simple Python function to be used in tasks
def print_hello():
    print("Hello, Iran, Israel, Indonesia!")

def print_task_name(task_name):
    print(f"Running task: {task_name}")

DEFAULT_ARGS = {
    "owner": "faishalrayyan",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}

# Define the DAG
dag = DAG(
    dag_id='simple_test_dag',
    description='A simple test DAG for Airflow',
    default_args=DEFAULT_ARGS,
    schedule_interval="0 * * * *",  # Set to None for manual triggering
    start_date=datetime(2024, 11, 21),
    catchup=False,
    tags=['dag1']
)

# Define the tasks

# Task 1: Print Hello World
task_hello = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag
)

# Task 2: Print task name
task_name = PythonOperator(
    task_id='print_task_name',
    python_callable=print_task_name,
    op_args=["Task 2: Print Task Name"],
    dag=dag
)

# Task 3: Print Hello World again
task_hello_again = PythonOperator(
    task_id='print_hello_again',
    python_callable=print_hello,
    dag=dag
)

# Task 4: Print another task name
task_name_again = PythonOperator(
    task_id='print_task_name_again',
    python_callable=print_task_name,
    op_args=["Task 4: Print Task Name Again"],
    dag=dag
)

# Set task dependencies (for example, task_hello -> task_name -> task_hello_again -> task_name_again)
task_hello >> task_name >> task_hello_again >> task_name_again