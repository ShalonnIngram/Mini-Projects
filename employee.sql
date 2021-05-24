-- create table in postgres database terminal & uploaded csv file from desktop --

## SQL Data Transformation

```sql
dataengineering-# CREATE TABLE employee(id INTEGER, fname VARCHAR, lname VARCHAR, title VARCHAR, age INTEGER, wage MONEY, hire_date DATE);
```


dataengineering=# SELECT * FROM employee;
 id | fname | lname | title | age | wage | hire_date 
----+-------+-------+-------+-----+------+-----------
(0 rows)



dataengineering=# COPY employee
dataengineering-# FROM '/Users/cianikaingram/Desktop/Data/employee.csv'
dataengineering-# DELIMITER ',' CSV HEADER;

COPY 1000



dataengineering=# SELECT * FROM employee;

  id  |    fname    |      lname       |   title   | age |  wage   | hire_date  
------+-------------+------------------+-----------+-----+---------+------------
    1 | Heath       | Pengilly         |           |  30 |  $32.00 | 2019-07-20
    2 | Madison     | MacCaughan       |           |  25 |  $63.00 | 2016-03-30
    3 | Ekaterina   | Hurt             |           |  37 |  $60.00 | 2021-03-23
    4 | Elsinore    | Ruusa            | Honorable |  52 |  $45.00 | 2018-09-14
    5 | Korrie      | Fortnon          | Honorable |  40 |  $66.00 | 2019-11-02
    6 | Quentin     | Unstead          | Mrs       |  49 |  $28.00 | 2015-06-24
    7 | Candide     | MacKaig          |           |  63 |  $37.00 | 2016-05-28
    8 | Adrian      | Duiguid          | Rev       |  69 |  $26.00 | 2018-06-07
    9 | Chester     | Brack            | Ms        |  66 |  $73.00 | 2019-11-30
   10 | Malissa     | Pagan            |           |  44 |  $36.00 | 2016-12-31
  
  
  
-- categorize employees by hire date  
SELECT
	*,
	CASE
		WHEN hire_date >= '2020-01-01' THEN 'New'
		ELSE 'Standard'
	END AS employee_type
FROM employee
LIMIT 5;



-- replace null values from title column with none

SELECT 
	fname, 
	lname, 
	coalesce(title, 'none') as title
FROM 
	employee
LIMIT 5;



-- view all options for title

SELECT 
	title, 
	count(*)
FROM employee
GROUP BY 1;



-- replace title 'honorable' with 'null'
SELECT 
	fname,
	lname,
	NULLIF(title, 'Honorable') AS title
FROM 
	employee;

