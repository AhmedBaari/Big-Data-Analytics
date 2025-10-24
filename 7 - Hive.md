# Introduction to Apache Hive

Apache Hive is a data warehouse system built on top of Hadoop that provides a SQL-like interface for querying and managing large datasets stored in distributed storage. It allows users to write queries using HiveQL (Hive Query Language), which is similar to SQL, making big data analysis accessible without requiring extensive programming knowledge.[1]

## What is Hive?

Hive translates SQL-like queries into MapReduce jobs that run on Hadoop clusters, enabling efficient processing of massive datasets. It's particularly useful for batch processing, data summarization, and analytical queries on large-scale data. Hive organizes data into tables with defined schemas, similar to traditional relational databases, but is designed to handle petabytes of data across distributed systems.[1]

## Setting Up Your Environment

### Preparing Data Files

Before working with Hive, you need to prepare your data files locally. In the example, two CSV files are used:[1]

- `employees.csv` containing employee information (emp_id, name, dept_id, salary)
- `departments.csv` containing department information (dept_id, dept_name)

### Loading Data into HDFS

Hive reads data from the Hadoop Distributed File System (HDFS). First, create a directory in HDFS to store your data files:[1]

```bash
hdfs dfs -mkdir -p /user/hive/data
```

Next, upload your CSV files from the local filesystem to HDFS:

```bash
hdfs dfs -put employees.csv /user/hive/data/
hdfs dfs -put departments.csv /user/hive/data/
```

To verify that your files were uploaded successfully, list the contents of the directory:

```bash
hdfs dfs -ls /user/hive/data/
```

### Starting Hive

Launch the Hive command-line interface by typing:

```bash
hive
```

You'll see a `hive>` prompt where you can execute HiveQL commands.[1]

## Loading Data into Hive Tables

Once you have tables created in Hive, load your data from HDFS using the `LOAD DATA` command:

```sql
LOAD DATA INPATH '/user/hive/data/employees.csv' INTO TABLE employees;
LOAD DATA INPATH '/user/hive/data/departments.csv' INTO TABLE departments;
```

This command moves data from the specified HDFS path into your Hive table. Note that the data is moved, not copied, so it will no longer exist at the original HDFS location.[1]

## Basic Query Operations

### Selecting All Records

To retrieve all data from a table:

```sql
SELECT * FROM employees;
```

This displays all columns and rows from the employees table. The output shows employee IDs, names, department IDs, and salaries.[1]

### Selecting Specific Columns

To retrieve only certain columns:

```sql
SELECT name, salary FROM employees;
```

This query returns just the name and salary columns, making the output more focused.[1]

### Filtering with WHERE Clause

To filter records based on conditions:

```sql
SELECT * FROM employees WHERE salary > 55000;
```

This returns only employees whose salary exceeds 55,000. The result includes employees like Alice and Carol who meet this criterion.[1]

## Advanced Query Operations

### Joining Tables

Joins combine data from multiple tables based on related columns:

```sql
SELECT e.emp_id, e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id;
```

This query matches employees with their department names by joining on the common `dept_id` column. The result shows each employee along with their department name (HR, IT, or Finance).[1]

### Aggregation with GROUP BY

To calculate summary statistics:

```sql
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id;
```

This computes the average salary for each department. The results show department 10 has an average of 65,000, department 20 has 52,500, and department 30 has 40,000.[1]

### Sorting with ORDER BY

To sort results in ascending or descending order:

```sql
SELECT * FROM employees ORDER BY salary DESC;
```

This arranges employees by salary from highest to lowest. Carol appears first with 70,000, followed by Alice with 60,000.[1]

## Understanding Query Execution

Hive queries that involve complex operations like joins, aggregations, or sorting are converted into MapReduce jobs. These jobs run across the Hadoop cluster, which is why you'll see execution logs showing:[1]

- Job IDs and tracking URLs
- Number of mappers and reducers
- CPU time and progress percentages
- HDFS read/write statistics

Simple queries that only scan data may run faster without launching full MapReduce jobs. Understanding this execution model helps you appreciate why certain queries take longer to complete.[1]

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51316245/be4d3da7-5163-4995-bc1e-2a8d1d773876/BDA-Hive-Exp-6.pdf)
