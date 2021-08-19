import logging
import datetime
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
from airflow.operators.python_operator import PythonOperator


# Change these to your identifiers, if needed.
GOOGLE_CONN_ID = "google_cloud_storage_default"
POSTGRES_CONN_ID = "postgres_default"
POSTGRES_TABLE = "Table_Name"
BUCKET_NAME = "region-zone-airflow-12345-bucket"

def copy_to_gcs(table_name, file_name, bucket_name):
    gcs_hook = GoogleCloudStorageHook(GOOGLE_CONN_ID)
    pg_hook = PostgresHook.get_hook(POSTGRES_CONN_ID)
    
    logging.info("Exporting query to file '%s'", file_name)
    pg_hook.bulk_dump(table_name, tmp_file=file_name)
    
    logging.info("Uploading to %s/%s", bucket_name, file_name)
    gcs_hook.upload(bucket_name, file_name, file_name)
    

with DAG(
    dag_id="postgres_hook_dag_heroku",
    start_date=datetime.datetime(2020, 2, 2),
    schedule_interval=None,
    catchup=False,
) as dag:
    copy_to_gcs_task = PythonOperator(
        task_id="copy_to_gcs",
        python_callable=copy_to_gcs,
        op_kwargs={
            "table_name":  POSTGRES_TABLE,
            "file_name": POSTGRES_TABLE + ".tsv",
            "bucket_name": BUCKET_NAME
			}
        )
    copy_to_gcs
