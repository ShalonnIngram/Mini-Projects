In this project, I created a simple ETL workflow with Alteryx combining a csv and xlsx files containing dummy ordering data. 


# 1. Extraction 
During this step I extracted data from a both a Excel and csv files. In larger workflows, data will be extracted from various sources such as AWS S3 buckets, databases, zip files, and json files to name a few. During the extraction phase, I merged the datasets based on positon.

![extraction](https://user-images.githubusercontent.com/32176320/130826047-01c0ce86-f548-40bb-bdc4-7dd01a81822a.png)

# 2. Transformation
After I merged the files, I looked at the data profile to for data standardization and noticed the State field has different various of the state Georgia. 

![ga_various](https://user-images.githubusercontent.com/32176320/130826687-8ddfc1fa-91f5-457a-8630-b0e74fb896a3.png)
