"""A liveness prober dag for monitoring composer.googleapis.com/environment/healthy."""
from ast import With
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta
from airflow.operators.python import PythonOperator
from airflow.operators import mysql_operator
from pipeline.Trainer.training import ANN

default_args = {
    "owner": "machine-learning",
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


def train_model():
    cf = ANN()
    model = cf._training_model("model/")
    return model

with DAG(
    'Schedule_train',
    default_args=default_args,
    description='daily_training_model',
    schedule_interval="0 10 * * *",
    dagrun_timeout=timedelta(minutes=20),
    catchup=False,
    tags=["test"]
    ) as dag:

    @task(task_id="train_model")
    def train_model():
        """Print the Airflow context and ds variable from the context."""
        cf = ANN()
        model = cf._training_model("model/")
        return model

    task_read_data = mysql_operator(
        task_id='drop_table_mysql_external_file',
        sql='/scripts/drop_table.sql',
        dag=dag,
    )

    t2 = PythonOperator(
        task_id='train model',
        bash_command='echo test',
        dag=dag,
        depends_on_past=False,
    )

    task_save_to_db = mysql_operator(
        task_id='insert_to_db',
        sql='/scripts/drop_table.sql',
        dag=dag,
    )

    task_train_model = train_model()

    task_read_data >> task_train_model >> task_save_to_db
