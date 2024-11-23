from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

DEFAULT_ARGS = {
    "owner": "faishalrayyan",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}

# Define the DAG
dag = DAG(
    dag_id="daily_bash_dag",  # DAG ID
    description="A DAG that runs a bash command once a day",
    default_args=DEFAULT_ARGS,
    schedule="@daily",  # Run once a day at midnight
    start_date=datetime(2024, 1, 1),  # Start date for the DAG
    catchup=False,
    tags=["dag4"],
)

# Define the task that runs the bash command
bash_task = BashOperator(
    task_id="bash_task",  # Task ID
    bash_command='echo "This task runs once a day!"',  # Command to run
    dag=dag,  # The DAG the task belongs to
)

# The task will run once a day as per the schedule
