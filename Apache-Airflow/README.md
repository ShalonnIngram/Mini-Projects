Followed Udemy Course

Based on a 

# Use Case
- A Logistics Company has hundreds of vehicles on the road 
- Each vehicle has sensors that collects data about the state of the vehicle and reports every minute
- Data is uploaded to Google Cloud Storage every hour in CSV format via a cellular network
- Analysts want to consistently see the latest state of each vehicle to identify potential issues & historical data for full analysis

BUILD A DIAGRAM
Airflow
csv's --> google cloud storage bucket --> load to bigquery (data warehouse) --> create a table that will show most recent state of vehicle for analyts



# Load Data to a Data Warehouse
- I created storage buckets and uploaded csv files. I then created a Google Cloud connection to Airflow.

# Analyzed Data using PySpark

# Extended AIrflow with Custom Plugins

# Tested Airflow DAGS

# Put Airflow in Production


Use Google Cloud


# Use Case 2
Logistics Company
Data Scientists sent PySpark jobs
PySpark jobs need to run daily at 8pm
Different jobs on weekdays & weekends
Source data & output data are BigQuery tables
