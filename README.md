
This repo is a demonstration of my understanding of back- to front-end data processing, anayltics, and delivery (ETLs)

It comprises a back-end:
    - database setup (SQLAlchemy ORM table models)
    - data migration from source to warehouse (db)
    - transformations and derived, highly-available tables

As well as an API layer implemented with FastAPI:
    - main API script
    - pydantic 'schemas' to define API transactions
    - crud functions with endpoints

In order to populate a front-end:
    - streamlit 'server' accesses the running API 'server'
    - database can be wherever; as long as the API is open, the front-end can pull the data without incident.


This project is built to showcase:
    - focus on delivering insights; we take care of the back-end so you can get what you need up front
    - abstraction of system design and practical code modularity
    - end-to-end data workflow, from source to delivery; similar to real-world cloud applications

...as well as being a great learning experience for me!

# Database Setup and Functionality
`models.py` holds SQLAlchemy ORM models/database table schemas
`database.py` holds the engine and SessionLocal variables which instantiate and power our SQLALchemy Database
`my_url.py` is a secrets file
`dunnhumby.db` is the extracted database

# API Functionality
`schemas.py` for the API transaction definitions; FastAPI/pydantic data models/schemas
`main.py` holds the FastAPI application with API endpoints
`crud.py` holds endpoint functions


# ETL Tool
`dunnhumby_data_warehouse.py` holds DunnHumbyDataWarehouse, a class to handle data migration/extraction to the data warehouse
    - from data source into a data lake
        - in this case the sources are .csv files; could be a s3 bucket or event-based data; being returned/posted to the API

    - from data lake into data warehouse
        - Through automated/CRON jobs, produce highly-available insights from the data lake
        - Customer-/household-level analytics and profile 
        - Recommendations/Modelling  table
    
    - from data warehouse to front-end
        - Deliverable is a streamlit app which calls to the FastAPI server we've set up
