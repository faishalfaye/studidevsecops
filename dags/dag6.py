from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


def my_python_function():
    """A simple Python function that can be a task in your DAG."""
    print("This is a Python function executed as part of the DAG.")


# Default arguments for the DAG
default_args = {
    "owner": "faishal_rayyan",
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
}

# Define the DAG
with DAG(
    "example_dag",
    default_args=default_args,
    description="An example DAG to demonstrate code formatting with flake8 and Black.",
    schedule="* * * * *",
    catchup=False,
    tags=["dag6"],
) as dag:

    # Define the Python task
    python_task = PythonOperator(
        task_id="python_task", python_callable=my_python_function
    )

    # Define a Bash task
    bash_task = BashOperator(
        task_id="bash_task", bash_command="echo 'Hello from Bash!'"
    )

    # Set task dependencies (order of execution)
    python_task >> bash_task
