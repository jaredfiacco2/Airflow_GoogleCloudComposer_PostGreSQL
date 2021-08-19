import logging
import datetime
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
import csv


# Change these to your identifiers, if needed.
GOOGLE_CONN_ID = "google_cloud_storage_default"
POSTGRES_CONN_ID = "postgres_default"
BIGQUERY_CONN_ID = "bigquery_default"
GS_PATH = "gs://BUCKETNAME/"
TABLE_ARRAY = [ "POSTGRE_TABLE_1", 
                # "POSTGRE_TABLE_2",
]
BUCKET_NAME = "region-zone-airflow-12345-bucket"

def copy_to_gcs():
    for table in TABLE_ARRAY:
        gcs_hook = GoogleCloudStorageHook(GOOGLE_CONN_ID)
        pg_hook = PostgresHook.get_hook(POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()
        cursor.execute("select * from " + table)
        result = cursor.fetchall()
        with open(table +'.csv', 'w') as fp:
            a = csv.writer(fp, quoting = csv.QUOTE_MINIMAL, delimiter = ',')
            a.writerow([i[0] for i in cursor.description])
            a.writerows(result)
        logging.info("Uploading to bucket, " + table + ".csv")
        gcs_hook.upload(BUCKET_NAME, GS_PATH +table + ".csv", table + ".csv")
    gcp_to_bq_task


with DAG(
    dag_id="postgre_table_to_gcs_csv",
    start_date=datetime.datetime(2020, 2, 2),
    schedule_interval=None,
    catchup=False,
) as dag:
    copy_to_gcs_task = PythonOperator(
        task_id="copy_to_gcs",
        python_callable=copy_to_gcs,
        )
    gcp_to_bq_task = GoogleCloudStorageToBigQueryOperator(   
        task_id = 'gcp_to_bq_Table1',
        bucket = BUCKET_NAME,  
        source_objects = ["data/bugtrackerHerokuProdPostgre/bug_bug.csv"],
        destination_project_dataset_table = 'airflow_test.bug_bug',
        schema_fields = [
            #Edit to match your table's schema
            {'name':    'id',               'type': 'INTEGER',  'mode':   'REQUIRED'},
            {'name':    'title',            'type': 'STRING',   'mode':   'NULLABLE'},
            {'name':    'description',      'type': 'STRING',   'mode':   'NULLABLE'},
        ],
        write_disposition='WRITE_TRUNCATE',
        skip_leading_rows = 1,
        allow_quoted_newlines = True
        )

    copy_to_gcs

