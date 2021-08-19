
<!-- PROJECT SHIELDS -->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jaredfiacco2/SQLServer_GenerateDagsWithMetadata">
    <img src="images/airflow_logo.png" alt="Logo" width="345" height="146">
  </a>

  <h3 align="center">Airflow Dags for Bringing Postgre Data to Google Cloud</h3>

  <p align="center">
    Airflow Dags to make it easier to transfer data from one place to another all while having full oversight of the data pipeline. In this project, I take tables/queries from a Postgre instance and transfer them to a Google Cloud Storage Bucket as a CSV or TSV. I also show how you can kick it up an notch and transfer the CSV to a BigQuery Table.
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

- I wanted to set up a process where I can automatically bring all my data from a Postgres instance to a Google Cloud Storage bucket and then transfer the CSV files to Google Cloud BigQuery for analytics/warehousing. 

- Note: The data depicted in the gifs below is from one of my personal servers.

<img src="images\Overview.png" alt="Overview"/>

### Built With

* [Python](https://python.org)
* [Apache Airflow](https://airflow.apache.org/)
* [Postgres](https://www.postgresql.org/)
* [Google Cloud Storage](https://cloud.google.com/storage)
* [Google Cloud Composer](https://cloud.google.com/composer)
* [Google BigQuery](https://cloud.google.com/bigquery)

### Prerequisites

1. Install Airflow Locally or make a Google Cloud Composer Instance (~$10-$12/day). Pros and cons below.
  - Local Airflow Instance
    - Pros:
      - Free
      - The new Docker image makes it a bit easier to build. 
      - Best if you're experienced and don't have money/want to spend money.
    - Cons: 
      - Adding a Ubuntu or other Linux distro VM on your computer can slow/overheat it unless it's a souped up PC.
      - Can be very confusing for a newby.
      - Many requirements, so it takes a while to set up (can be north of a full day's time).
  - GCP Cloud Composer 
    - Pros: 
      - If you have never used Google Cloud before, you can get a FREE $300 credit fro your first month, so this would be a free environment for the first ~15-20 days.
      - Reletively fast setup (~25 Mins to initialize)
      - Easiest set up by far!
      - All the GCP connections come preset. So you can run your dags with minimal connectino set up time.
      - The best choice if you're a newby with $10-$20 to burn on a weekend and are looking for experience.
    - Cons: 
      - Cost: $10-$12 USD/day
      - You can't build over time, need to focus and dedicate yourself to coding. Time is money.


2. Create your Postgres Connection

<img src="images\Connections.gif" alt="Airflow Connections" />

3. Test your new connection with the Airflow "Data Profiling" Tool 

<img src="images\DataProfiling.gif" alt="Airflow Data Profiling" />

5. Edit the dag(s) so they pull the right data from Postgres and push te right data in the right formats on Google Cloud.


4. In your Google Cloud Storage Instance (created for this airflow instance), upload these dags to the dag folder.

<img src="images\GoogleCloudStorage.gif" alt="Google Cloud Storage" />

5. Run the DAG(s). Read the Logs if the operation fails. Make sure the data got to the storage bucket and is in the right format.

<img src="images\GoogleCloudComposer_Airflow.gif" alt="Airflow" />

6. Check out BigQuery to make sure the CSV data got over (if you ran the postgre_table_to_gcs_to_bq dag)

<img src="images\BigQuery.gif" alt="BigQuery" />

<!-- CONTACT -->
## Contact

[Jared Fiacco](https://www.linkedin.com/in/jaredfiacco/) - jaredfiacco2@gmail.com

Project Link: [https://github.com/jaredfiacco2/BugTracker-Public](https://github.com/jaredfiacco2/BugTracker-Public)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
