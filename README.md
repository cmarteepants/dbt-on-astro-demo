# cosmos-demo

This repo contains a dbt project and an Astro proejct with a set of Airflow DAGs that show how to run dbt in Airflow using [Cosmos](https://github.com/astronomer/astronomer-cosmos).

To run this, you'll need:

- [The Astro CLI installed](https://docs.astronomer.io/astro/cli/overview)
- Docker

## Setup

1. Clone this repo
2. Run `cd astro` to move to the astro project
2. Run `astro dev start` to start the Airflow instance

## The DAGs

The DAGs in this repo are meant to illustrate how to run dbt in Airflow using Cosmos. They use dbt's jaffle_shop example project.

The DAGs fall into three categories:

- Basic: these are the simplest examples of Cosmos
- Profiles: these show how to customize your dbt profiles using Cosmos
- Filtering: these show how to use Cosmos to filter which models are run
