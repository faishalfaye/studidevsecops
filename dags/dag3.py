from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator

DEFAULT_ARGS = {
    "owner": "faishalrayyan",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}

# Define the DAG
dag = DAG(
    dag_id="daily_dummy_dag",  # DAG ID
    description="A dummy DAG that runs once a day",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",  # Run once a day at midnight
    start_date=datetime(2024, 1, 1),  # Start date for the DAG
    catchup=False,
    tags=["dag3"],
)

# Define the dummy task (no actual work is done)
dummy_task = DummyOperator(
    task_id="dummy_task",  # Task ID
    dag=dag,  # The DAG the task belongs to
)

# The task will run once a day as per the schedule
