# Address Storage 

## Overview
This project displays a very common data engineer task. There are multiple csv's (about 8 thousand rows) of address data uploaded to s3 daily. Once the csv file is present, a lambda function is triggered to start a glue job. During the initial setup, I used a glue crawler to crawler & infer the schema of the files in the s3 bucket, created a database & table. Once the glue job is executed, the glue ETL job takes the data, does some aggregation counts, converts the file into parquet, & stores the file in an output s3 bucket for storage. There is an option to query the data via athena is any analysis is needed. 

<br>

![Screenshot 2024-05-02 at 6 11 59 PM](https://github.com/ShalonnIngram/Mini-Projects/assets/32176320/e788ad19-0ccf-42ab-bc89-78c4bd069af6)



## Process
- The files are uploaded to s3 individually throughtout the day
- Once the file is present, a lambda function is triggered to begin Glue ETL job
- During the transformation, the data is aggregated by columns and converted into parquet format to be stored in another s3 bucket
- The data can be queryed via Athena for analysis 



### 1. AWS S3: Data Storage - Create a AWS S3 Bucket & load file
- Once the data is loaded into s3, the Lambda function is triggered to begin Glue job[Screenshot 2024-05-02 at 6 20 40 PM](https://github.com/ShalonnIngram/Mini-Projects/assets/32176320/23de0bc8-ec6f-4310-9fe8-40f5269fb9dc) to upload files from a specific directory to an S3 bucket
![Screen Shot 2021-06-24 at 11 18 03 AM](https://user-images.githubusercontent.com/32176320/123288837-eaf94e00-d4dd-11eb-8477-9a2b0a2761a2.png)

<br>

### 2. AWS EMR: Data Transformation - PySpark ETL Process
 - Once file is loaded in the S3 bucket, a [ is triggered which runs the [Pyspark script](https://github.com/ShalonnIngram/DataEngineering-Portfolio/blob/master/Loan%20Data%20Project/loan_data_transformation_script.py) on an EMR cluster for the ETL process. The data is cleaned, transformed into parquet files and returned to the S3 bucket in a `transformed` bucket


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

