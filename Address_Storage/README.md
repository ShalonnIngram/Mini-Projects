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



### 1. CSV file uploaded to S3 which triggers Lambda function 
- ![Screenshot 2024-05-02 at 6 39 14 PM](https://github.com/ShalonnIngram/Mini-Projects/assets/32176320/7af5fee7-f944-4436-a347-2ee77287b294)


  <br> 
  Once the data is loaded into s3, the Lambda function is triggered to begin Glue job                                                                                     
 ![Screenshot 2024-05-02 at 6 20 40 PM](https://github.com/ShalonnIngram/Mini-Projects/assets/32176320/23de0bc8-ec6f-4310-9fe8-40f5269fb9dc)
 here is the code using the boto3 package
![Screenshot 2024-05-02 at 6 24 04 PM](https://github.com/ShalonnIngram/Mini-Projects/assets/32176320/0b836312-ac72-4ed8-977e-b54dc772dd41)

<br>

### 2. AWS Glue to transform & convert file to parquet then store
 - The Glue ETL jobruns to create aggregation and convert to parquet ![Screenshot 2024-05-02 at 6 28 26 PM](https://github.com/ShalonnIngram/Mini-Projects/assets/32176320/a501ec74-2038-41d5-a475-1cc28659a4a9) transformed into parquet files and returned to the S3 bucket in a `output` bucket

<br>

### 3. Loaded into Athena for Querying & Analysis - Loaded into S3 for Storage

![Screenshot 2024-05-02 at 6 32 09 PM](https://github.com/ShalonnIngram/Mini-Projects/assets/32176320/ea28de29-a1e2-4f12-8c35-e75e0f0e09a8)

<br>
 
 ![Screenshot 2024-05-02 at 6 37 05 PM](https://github.com/ShalonnIngram/Mini-Projects/assets/32176320/e4c1f2fe-3e72-4fa4-aef4-2d29395f1a67)



