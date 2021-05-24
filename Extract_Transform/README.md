# Missed_Appointments


## Overview
I downloaded the [Kaggle](https://www.kaggle.com/joniarroba/noshowappointments) dataset via csv,
- loaded into a pandas dataframe
- completed data transformations via pandas
- loaded the data into a Postgres database
- used SQL to perform data analysis


## Extraction: 
I downloaded the [Kaggle](https://www.kaggle.com/joniarroba/noshowappointments) dataset via csv & used python pandas to import.

## Transforming: Python (Pandas)
After importing the data, I performed data transformations such as 
- configuring columns with scientific notation formats to integers
- splitting out Zulu timestamps into two columns and converting the time zone into the Eastern Timezone
- dropped unnecessary columns
- dropped duplicated
- renamed columns
- ensured datatypes were correct per columns' values

## Load: Postgres Database
I created the table & copied the csv with the transformed data into Postgres via the command line. I used psycopg2 & sqlalchemy to create a connection to the database where I performed data analysis via SQL/
