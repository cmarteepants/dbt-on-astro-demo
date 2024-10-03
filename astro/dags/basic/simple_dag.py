from datetime import datetime

from cosmos import DbtDag, ProjectConfig

from include.profiles import dwh_snowflake
from include.constants import jaffle_shop_path

simple_dag = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(jaffle_shop_path),
    profile_config=dwh_snowflake,
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="simple_dag",
    tags=["simple"],
    default_args={
        "owner": "airflow",
        "retries": 2
    },
)
