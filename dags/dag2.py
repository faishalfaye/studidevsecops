from airflow import DAG
from airflow.operators.python import PythonOperator

# Define a simple Python function to be used in the task
def print_hello():
    print("Hello, Airflow!")

DEFAULT_ARGS = {
    "owner": "faishalrayyan",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}

# Define the DAG
dag = DAG(
    dag_id='daily_hello_dag',  # DAG ID
    description='A simple DAG that prints hello once a day',
    default_args=DEFAULT_ARGS,
    schedule_interval='@daily',  # Run once a day at midnight
    start_date=datetime(2024, 1, 1),  # Start date for the DAG
    catchup=False,
    tags=['dag2']
)

# Define the task that will run the print_hello function
task = PythonOperator(
    task_id='hello_task',  # Task ID
    python_callable=print_hello,
    dag=dag,  # The DAG the task belongs to
)

# The task will run once a day as per the schedule
