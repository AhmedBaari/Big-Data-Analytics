This exercise demonstrates how to use Apache Hive to work with log data stored in Hadoop's distributed file system (HDFS) and perform various SQL-like operations on it.

### Step-by-step Explanation:

1. **Create a directory in HDFS to store logs**
   ```bash
   hdfs dfs -mkdir -p /user/cloudera/logs
   ```
   This command creates a folder `/user/cloudera/logs` in HDFS where the log file will be stored.

2. **Copy the log file from the local system to HDFS**
   ```bash
   hdfs dfs -put logs.txt /user/cloudera/logs/
   ```
   This uploads `logs.txt` from the local machine into the newly created HDFS directory.

3. **List files in HDFS directory to verify upload**
   ```bash
   hdfs dfs -ls /user/cloudera/logs/
   ```
   This lists the files inside `/user/cloudera/logs` to confirm the upload of `logs.txt`.

4. **Open Hive CLI**
   ```bash
   hive
   ```
   Start the Hive interactive shell to execute HiveQL commands.

5. **Create a Hive database for logs (if not existing)**
   ```sql
   CREATE DATABASE IF NOT EXISTS logdb;
   USE logdb;
   ```
   This sets up a new database named `logdb` and switches to it to organize tables related to logs.

6. **Create an external Hive table to map to the log data**
   ```sql
   CREATE EXTERNAL TABLE logs_structured (
       log_time STRING,
       log_level STRING,
       user STRING,
       action STRING
   )
   ROW FORMAT DELIMITED
   FIELDS TERMINATED BY ','
   LINES TERMINATED BY '\n'
   STORED AS TEXTFILE
   LOCATION '/user/cloudera/logs/';
   ```
   This creates a table `logs_structured` that reads log data from the HDFS folder directly. The table schema defines four string columns. The table expects CSV-format data with commas separating fields and newline separating records.

7. **Create views (virtual tables) for filtered data**

   - For error logs only:
     ```sql
     CREATE VIEW error_logs AS
     SELECT * FROM logs_structured
     WHERE log_level = 'ERROR';
     ```
     This creates a view `error_logs` that shows only logs with `log_level` as `ERROR`.

   - For user login actions:
     ```sql
     CREATE VIEW login_logs AS
     SELECT * FROM logs_structured
     WHERE action LIKE 'logged%';
     ```
     This creates a view `login_logs` for log entries where the action starts with "logged".

8. **Create an index on the log_level column to speed up queries**
   ```sql
   CREATE INDEX idx_log_level
   ON TABLE logs_structured (log_level)
   AS 'COMPACT'
   WITH DEFERRED REBUILD;

   ALTER INDEX idx_log_level ON logs_structured REBUILD;
   ```
   An index named `idx_log_level` is created on the `log_level` column. After creating the index with deferred rebuild, the index is rebuilt to take effect, which launches a MapReduce job. Indexes help speed up filtering queries based on `log_level`.

9. **Query the logs table**

   - Select all logs:
     ```sql
     SELECT * FROM logs_structured;
     ```
     Retrieves the entire log data.

   - Select only logs at INFO level:
     ```sql
     SELECT * FROM logs_structured WHERE log_level = 'INFO';
     ```
     Filters to show only INFO logs.

   - Count logs per user:
     ```sql
     SELECT user, COUNT(*) as total_logs
     FROM logs_structured
     GROUP BY user;
     ```
     Aggregates logs by user and counts how many entries each user has.

   - Query logs using views:
     ```sql
     SELECT * FROM error_logs;
     ```
     Queries the `error_logs` view to show only error-level logs.

### Summary

This exercise covers the full workflow of:

- Uploading data to HDFS
- Creating Hive databases and external tables mapped to data in HDFS
- Using HiveQL commands for filtering, aggregation, and joining-like queries
- Creating views for reusable query logic
- Using Hive indexing for performance optimization

It demonstrates how Hive acts as a SQL interface over big data stored in Hadoop, enabling easy querying and analysis of log data.

All code is executed in the Hive CLI environment and interacts with data stored in HDFS through the Hadoop ecosystem. This is a foundational example suitable for junior university students beginning with big data querying in Hive.[1]

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51316245/576e2215-cd37-4ab5-8dd3-04360b27990f/BDA-Hive-Exp-7.pdf)
