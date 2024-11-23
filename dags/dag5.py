from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator


# Define default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "email_on_failure": False,
    "email_on_retry": False,
}

# Initialize the DAG
dag = DAG(
    "simple_dag",  # DAG ID
    description="A simple dummy DAG",
    default_args=default_args,
    schedule_interval="@daily",  # Runs once per day
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["example"],
)

# Define the tasks
start_task = DummyOperator(
    task_id="start_task",  # Task ID
    dag=dag,  # The DAG this task belongs to
)

end_task = DummyOperator(
    task_id="end_task",  # Task ID
    dag=dag,  # The DAG this task belongs to
)

# Set the task dependencies
start_task >> end_task
