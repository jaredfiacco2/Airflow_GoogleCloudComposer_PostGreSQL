
<!-- PROJECT SHIELDS -->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jaredfiacco2/SQLServer_GenerateDagsWithMetadata">
    <img src="images/airflow_logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Airflow Dags for Bringing Postgre Data to Google Cloud</h3>

  <p align="center">
    Airflow Dags to make it easier to transfer data from . Complete with a Bredth First Search Algorithim that searches doe all nodes related to a single node. Very helpful for onboarding new engineers or reviewing the current state of a legacy server!
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

- As an Engineer working in multiple mature data warehouses, I'm acutely aware that being able to speak to established data flows and design lightweight queries is essential. It's the only way to develop high-quality code.

- While traversing through a new (to me) database, I knew there had to be a better way to wrap my head around the data-flows. So, I wrote some scripts that identify all objects (nodes) and dependencies (edges) in a Microsoft SQL server & visualize the resulting network in an interactive way.

- I also developed an SQL-based Breadth-First Search (BFS) filtering technique to pull all related nodes & edges from a single, or multiple starting nodes. This allows the user to target specific nodes and removes all unrelated nodes/edges, making the visualization run more smoothly. The BFS is pretty quick, even on Data Warehouses with >20k nodes.

- Big shout out to Mohit Mayank for making the open-source python library: [Jaal](https://github.com/imohitmayank/jaal). It made implementing an interactive network visualization much easier. Thank you!

- Note: The server depicted in the gif below is my personal server.

<img src="images\demo.gif" alt="Demo"/>

### Built With

* [Python](https://python.org)
* [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
* [Jaal](https://github.com/imohitmayank/jaal)

### Prerequisites

1. Installing all Required Packages
  ```sh
  pip install -r requirements.txt
  ```

2. In SSMS, Create Database Called "DataDocumentation". 

3. Create Service Account & Role
    - Service Account
        - In Server Secutiry, create a Service Account
        - Take note of the Username and password, you will use this to update the credentials in runDataDocVisual.py 
    - Role
        - In the DataDocumentation database, 

4. Open the SQL folder, run each of the files
    - First, run "Table_D.sql" files
    - Next, run "vView.sql" files
    - Finally, fun "StoredProcedures_SP" files

5. Update Server Acces Credentials in runDataDocVisual.py  

6. Target a specific node of interest vs show all nodes in server
    - To Target a node of interest, run the "Filter_EdgesAndNodes_StartingNodeLikeParam_SP" stored procedure. Input the table name or partial table name as the parameter. 
    ```
    # For For A Specific Node of Interest
    python runDataDocVisual_Filtered.py
    ```

    ```
    # For All Nodes Of Interest
    python runDataDocVisual.py
    ```


<!-- CONTACT -->
## Contact

[Jared Fiacco](https://www.linkedin.com/in/jaredfiacco/) - jaredfiacco2@gmail.com

Project Link: [https://github.com/jaredfiacco2/BugTracker-Public](https://github.com/jaredfiacco2/BugTracker-Public)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jaredfiacco/
[features-oauth]: images/BugTrackerTools_Oauth.gif
[features-api]: images/BugTrackerTools_API.gif
[features-clickup]: images/BugTrackerTools_V05.gif
[features-dashboard]: images/BugTrackerTools_Dashboard_V01.gif
[features-workqueue]: images/BugTrackerTools_Workqueue.gif