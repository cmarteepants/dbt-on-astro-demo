from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles import SnowflakeEncryptedPrivateKeyPemProfileMapping

from include.constants import jaffle_shop_path

dbt_profile_overrides = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(jaffle_shop_path),
    profile_config=ProfileConfig(
        # these map to dbt/jaffle_shop/profiles.yml
        profile_name="jaffle_shop",
        target_name="prod",
        profile_mapping=SnowflakeEncryptedPrivateKeyPemProfileMapping(
            conn_id="dwh_snowflake",
        ),
    ),
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="dbt_profile_overrides",
    tags=["profiles"],
)
