from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "mlops",
    "depends_on_past": False,
    "start_date": datetime(2025, 5, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG("ml_pipeline", default_args=default_args, schedule_interval="@daily") as dag:
    t1 = BashOperator(task_id="scrape", bash_command="python scripts/scrape_web.py")
    t2 = BashOperator(task_id="preprocess", bash_command="python scripts/preprocess.py")
    t3 = BashOperator(task_id="train", bash_command="python scripts/train_rf.py")
    t4 = BashOperator(task_id="deploy", bash_command="bash scripts/deploy.sh")
    t1 >> t2 >> t3 >> t4
