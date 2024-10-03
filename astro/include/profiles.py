"Contains profile mappings used in the project"
import os
from cosmos import ProfileConfig
from cosmos.profiles import SnowflakeEncryptedPrivateKeyPemProfileMapping

def build_profile_config(
    profile_name: str = "jaffle_shop",
    env: str = os.environ["ENV"],
    conn_id="dwh_snowflake"
) -> ProfileConfig:

    if env == "dev":
        return ProfileConfig(
            profile_name=profile_name,
            target_name=env,
            profiles_yml_filepath="/usr/local/airflow/dbt/profiles.yml"
        )

    if env == "prod":
        return ProfileConfig(
            profile_name=profile_name,
            target_name=env,
            profile_mapping=SnowflakeEncryptedPrivateKeyPemProfileMapping(conn_id=conn_id)
        )

    raise ValueError(f"Invalid environment: {env}")

dwh_snowflake = build_profile_config()
