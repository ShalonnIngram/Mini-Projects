# Loan Data Project

## Overview
As a Data Engineer, I was tasked with building an ETL Data Pipeline for the loan department which included analysts and scientists. During discovery, it was uncovered that the analysts where spending hours, downloading, reformatting, and cleaning csv files downloaded from the proprietary system. As the data is growing, this process is no longer viable as the files are becoming too large to open on the analyts computers. The request was to create a pipeline that saves files, automates the cleaning process & make the data accessible for data scientists to perform machine learning models and analysts to continue to find insights.\
**Data Source**: LendingClub Loan Data 2007 - Q3 2019 (acceptence file) [Kaggle Data Set](https://www.kaggle.com/denychaen/lending-club-loans-rejects-data?select=appl_accepted_20072019Q3.csv)

<br>

![Untitled Diagram](https://user-images.githubusercontent.com/32176320/125023790-91e8f880-e04d-11eb-8367-0142c69d5785.png)



## Process
- The file is automatically uploaded to a AWS S3 
- Data is transformed & exported into parquet files via Pyspark on AWS EMR, this automated via a AWS Lambda script
- Cleaned data is returned to S3 bucket
- Data is registered in Glue Data Catalog with Glue Crawler creating the 
- Glue ETL job allows data to be accessed via AWS Redshift Spectrum
- Data is connected to Tableau (BI Tool)



### 1. AWS S3: Data Storage - Create a AWS S3 Bucket & load file
- [auto_file_s3_uploader](https://github.com/ShalonnIngram/DataEngineering-Portfolio/blob/master/Loan%20Data%20Project/auto_file_s3_uploader.py) to upload files from a specific directory to an S3 bucket
![Screen Shot 2021-06-24 at 11 18 03 AM](https://user-images.githubusercontent.com/32176320/123288837-eaf94e00-d4dd-11eb-8477-9a2b0a2761a2.png)

<br>

### 2. AWS EMR: Data Transformation - PySpark ETL Process
 - Once file is loaded in the S3 bucket, a [AWS Lambda script](https://github.com/ShalonnIngram/DataEngineering-Portfolio/blob/master/Loan%20Data%20Project/trigger_emr_step.py) is triggered which runs the [Pyspark script](https://github.com/ShalonnIngram/DataEngineering-Portfolio/blob/master/Loan%20Data%20Project/loan_data_transformation_script.py) on an EMR cluster for the ETL process. The data is cleaned, transformed into parquet files and returned to the S3 bucket in a `transformed` bucket


`loan_amnt`: borrower's total loan amount range - ($500 to $40k)\
`term`: number of borrower's payments range: (36 or 60 months)\
`int_rate`: borrower's interest rate on the loan range: (5.42% to 30.89%) \
`installment`: borrower's monthly payment\
`emp_length`: borrower's employment length - various\
`home_ownership`: borrower's living arrangements - (mortgage, renting, other)\
`annual_inc`: borrower's annual income (0 means less than 1 year)\
`loan_status`: current state of the loan\
`addr_state`: state of applicant/borrower\
`dti`: debt to income ratio of borrower - total debt divided by reported income\
`last_fico_range_high`: highest last reported fico score of borrower\
`application_type`: identifies whether applicant is an individual or joint/co-borrower\
`tot_cur_bal`: total debt balance of borrower at the time of application\
`purpose`: applicant's purpose for the loan (credit_card, debt_consolidation, other)
 <br>
 
 #### Data Cleaning Process: PySpark
 - Select specific columns - 14 out of 159
 - Drop null columns
 - Remove special characters & strings vis regrex
 - Removed unnecessary digits
 - Created new date columns 
 - Updated schema
 - Transformed csv to parquet files for faster performance:
![Screen Shot 2021-07-08 at 8 50 35 PM](https://user-images.githubusercontent.com/32176320/125012961-06656c80-e039-11eb-8f98-9217e366d02b.png)

<br>

### 3. AWS Redshift Spectrum: Date Warehouse - Redshift Cluster, Glue Crawler, Glue Data Catalog, Glue ETL
Use Glue Crawler to crawl S3 bucket data  
The crawler returned the schema and populated the Glue Data Catalog

 - Create Redshift Cluster
 ![Screen Shot 2021-07-08 at 8 48 44 PM](https://user-images.githubusercontent.com/32176320/125014437-b76d0680-e03b-11eb-8d44-4383dad2c135.png)

 - Created schema in AWS Redshift Spectrum
 
 `create external schema spectrum_schema from data catalog`\
 `database 'loan-project'`\
 `iam_role 'arn:aws:iam::508580821825:role/redshiftSpectrumRole'`\
 `create external database if not exists;`	
<br>
<br>
- [Glue ETL script](https://github.com/ShalonnIngram/DataEngineering-Portfolio/blob/master/Loan%20Data%20Project/glue_load_data_script.py) was created to load data into AWS Redshift for querying

![Screen Shot 2021-07-08 at 8 49 49 PM](https://user-images.githubusercontent.com/32176320/125013079-33b21a80-e039-11eb-87dc-247f8b73245f.png)

<br>
<br>

### 4. Tableau: Connect to BI tool
![Screen Shot 2021-07-08 at 10 32 58 PM](https://user-images.githubusercontent.com/32176320/125014891-7d503480-e03c-11eb-90ba-fd7e89de7735.png)




Tools: Jupyter Notebook, Pycharm
Environment : Docker, Virtual Environment, AWS CLI
![Screen Shot 2021-07-08 at 9 25 46 PM](https://user-images.githubusercontent.com/32176320/125009804-4164a180-e033-11eb-9462-e718cd568a9b.png)

