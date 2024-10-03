from cosmos.operators import DbtDocsS3Operator
from include.profiles import dwh_snowflake
from airflow import DAG
from datetime import datetime


with DAG(
    dag_id="generate_docs_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={"retries": 2},
):

    generate_dbt_docs_aws = DbtDocsS3Operator(
        task_id="generate_dbt_docs_aws",
        project_dir="/usr/local/airflow/dbt",
        profile_config=dwh_snowflake,
        # docs-specific arguments
        connection_id="s3_cmartineau",
        bucket_name="cmartineau",
    )