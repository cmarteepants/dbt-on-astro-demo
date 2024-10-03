from cosmos.operators import DbtDocsS3Operator
# from airflow import DAG

from include.constants import jaffle_shop_path
from include.profiles import dwh_snowflake

generate_dbt_docs_aws = DbtDocsS3Operator(
    task_id="generate_dbt_docs_aws",
    project_dir=jaffle_shop_path,
    profile_config=dwh_snowflake,
    # docs-specific arguments
    connection_id="s3_cmartineau",
    bucket_name="cmartineau",
)