from datetime import datetime

from cosmos import DbtDag, ProjectConfig, RenderConfig

from include.profiles import dwh_snowflake
from include.constants import jaffle_shop_path

customers_tag = DbtDag(
    project_config=ProjectConfig(jaffle_shop_path),
    profile_config=dwh_snowflake,
    # new render config
    render_config=RenderConfig(
        select=["tag:customers"],
    ),
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="customers_tag",
    tags=["filtering"],
)
