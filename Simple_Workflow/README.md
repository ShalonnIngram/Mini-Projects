In this project, I created a simple ETL workflow with Alteryx combining .csv and .xlsx files containing dummy ordering data. I extracted, merged, transformed/cleaned and reported the frequency of items ordered. I also automated this report to be ran and produced daily at 10:00AM to avoid end users running it manually.

* I would recommend a visual of the report by my trial did not come with reporting capabilities.

# 1. Extraction 
During this step I extracted data from a both a Excel and csv files. In larger workflows, data will be extracted from additional sources such as AWS S3 buckets, databases, zip files, and json files to name a few. During the extraction phase, I merged the datasets based on positon.

![extraction](https://user-images.githubusercontent.com/32176320/130826047-01c0ce86-f548-40bb-bdc4-7dd01a81822a.png)

# 2. Transformation
After I merged the files, I looked at the data profile to for data standardization and noticed the State field has different variations of the state Georgia. 

![ga_various](https://user-images.githubusercontent.com/32176320/130826687-8ddfc1fa-91f5-457a-8630-b0e74fb896a3.png)

Data Cleansing
- removed null values
- removed null columns
- removed whitespaces
- removed punctuation

# 3. Load
This data returns a .csv file with the freqency of orders by item name
![Screen Shot 2021-08-25 at 1 16 19 PM](https://user-images.githubusercontent.com/32176320/130837630-ff146989-be0b-4739-9e24-7be84d4f319d.png)

# 4. Automation
To avoid end users from manually running this report, I automated it to run daily at 10:00AM.

- Create the task <br>
![Screen Shot 2021-08-25 at 1 10 55 PM](https://user-images.githubusercontent.com/32176320/130837400-132cced8-4843-4d23-b2e0-fdbd318e6f3b.png)

- Create the action to perform <br>

![Screen Shot 2021-08-25 at 1 12 50 PM](https://user-images.githubusercontent.com/32176320/130837451-e13f59b4-3ea0-401d-9a1b-de3d29a0684d.png)

- Schedule the task <br>

![Screen Shot 2021-08-25 at 1 13 44 PM](https://user-images.githubusercontent.com/32176320/130837570-e5fc4101-a37c-43ac-a1d3-7c5b533986dd.png)
<br>
- Result Summary

![Screen Shot 2021-08-25 at 1 26 11 PM](https://user-images.githubusercontent.com/32176320/130837734-a005bba8-3641-40a1-905c-a736af512168.png)
