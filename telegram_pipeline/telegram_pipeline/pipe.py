from dagster import op, job
import subprocess

@op
def scrap_messages():
    subprocess.run(["python" , "../scripts/scrap_message.py"] , check=True)

@op
def load_raw_to_postgres():
    subprocess.run(["python" , "../scripts/load_to_postgres.py"] , check=True)

@op
def run_dbt_transformations():
    subprocess.run(["dbt", "run", "--project-dir", "../src/dbt"], check=True)

@job
def telegram_pipeline_job():
    scrap_messages()
    load_raw_to_postgres()
    run_dbt_transformations()
    