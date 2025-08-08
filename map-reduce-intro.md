# Hadoop MapReduce with Cloudera: Step-by-Step Guide

This guide walks you through running Python MapReduce jobs on Hadoop using Cloudera, covering three exercises: **wordcount**, **bigram count**, and **finding the coolest year** from temperature data. It also explains the concepts, commands, and common issues.

---

## What is Hadoop?

**Hadoop** is an open-source framework for distributed storage and processing of large datasets across clusters of computers.  
- **HDFS (Hadoop Distributed File System):** Stores data across multiple machines.
- **MapReduce:** A programming model for processing large data sets with a distributed algorithm.

## What is Cloudera?

**Cloudera** is a platform that simplifies the deployment, management, and monitoring of Hadoop and related big data tools. It provides a user-friendly interface and enterprise features.

---

## Why Use Hadoop and MapReduce?

- **Scalability:** Handles large datasets efficiently.
- **Fault Tolerance:** Data is replicated across nodes.
- **Parallel Processing:** Tasks are distributed for faster computation.

---

## Initial Steps

1. **Access Cloudera Quickstart VM or Cluster.**
2. **Open Terminal.**
3. **Prepare your input data and Python scripts.**

---

## HDFS Basics

- **Upload files to HDFS:**  
  ```
  hdfs dfs -mkdir -p /user/cloudera/input
  hdfs dfs -put /home/cloudera/baari/input.txt /user/cloudera/input/
  ```
- **List files in HDFS:**  
  ```
  hdfs dfs -ls /user/cloudera/input
  ```
- **Remove output directory before rerunning jobs:**  
  ```
  hdfs dfs -rm -r /user/cloudera/output
  ```

---

## 1. Wordcount MapReduce

### Mapper (`mapper.py`)
````python
#!/usr/bin/env python
import sys
for line in sys.stdin:
    for word in line.strip().split():
        print("%s\t1" % word)
````

### Reducer (`reducer.py`)
````python
#!/usr/bin/env python
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)
    if word == current_word:
        current_count += count
    else:
        if current_word:
            print("%s\t%d" % (current_word, current_count))
        current_word = word
        current_count = count

if current_word:
    print("%s\t%d" % (current_word, current_count))
````

### Run the Job
```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -input /user/cloudera/input/input.txt \
    -output /user/cloudera/output \
    -mapper "python mapper.py" \
    -reducer "python reducer.py" \
    -file /home/cloudera/baari/mapper.py \
    -file /home/cloudera/baari/reducer.py
```

### View Results
```
hdfs dfs -cat /user/cloudera/output/part-00000
```

---

## 2. Bigram Count MapReduce

### Mapper (`mapper.py`)
````python
#!/usr/bin/env python
import sys

for line in sys.stdin:
    words = line.strip().split()
    for i in range(len(words) - 1):
        bigram = "%s %s" % (words[i], words[i+1])
        print("%s\t1" % bigram)
````

### Reducer (`reducer.py`)
````python
#!/usr/bin/env python
import sys

current_bigram = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    bigram, count = parts
    try:
        count = int(count)
    except ValueError:
        continue
    if bigram == current_bigram:
        current_count += count
    else:
        if current_bigram:
            print("%s\t%d" % (current_bigram, current_count))
        current_bigram = bigram
        current_count = count

if current_bigram:
    print("%s\t%d" % (current_bigram, current_count))
````

---

## 3. Coolest Year from Temperature Data

### Sample Input (`input.txt`)
```
2015,22
2016,18
2017,25
...
```

### Mapper (`mapper.py`)
````python
#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    if line == "" or line.startswith("year"):
        continue
    parts = line.split(',')
    if len(parts) != 2:
        continue
    year, temp = parts
    print("%s\t%s" % (year, temp))
````

### Reducer (`reducer.py`)
````python
#!/usr/bin/env python
import sys

current_year = None
total_temp = 0
count = 0

coolest_year = None
coolest_avg = None

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    year, temp = parts
    try:
        temp = float(temp)
    except ValueError:
        continue
    if year == current_year:
        total_temp += temp
        count += 1
    else:
        if current_year:
            avg_temp = total_temp / count
            if coolest_avg is None or avg_temp < coolest_avg:
                coolest_year = current_year
                coolest_avg = avg_temp
        current_year = year
        total_temp = temp
        count = 1

if current_year:
    avg_temp = total_temp / count
    if coolest_avg is None or avg_temp < coolest_avg:
        coolest_year = current_year
        coolest_avg = avg_temp

if coolest_year:
    print("%s\t%.2f" % (coolest_year, coolest_avg))
````

---

## Common Issues & Fixes

### 1. **Python Syntax Errors**
- **Issue:** f-strings not supported in Python 2.
- **Fix:** Use `%` formatting instead.

### 2. **Output Directory Exists**
- **Issue:** Hadoop job fails if output directory exists.
- **Fix:**  
  ```
  hdfs dfs -rm -r /user/cloudera/output
  ```

### 3. **Script Not Executable**
- **Issue:** Mapper/Reducer scripts not running.
- **Fix:**  
  ```
  chmod +x /home/cloudera/baari/mapper.py
  chmod +x /home/cloudera/baari/reducer.py
  ```

### 4. **No Output**
- **Issue:** Input format mismatch, empty input, or logic errors.
- **Fix:**  
  - Check input file format.
  - Test scripts locally:
    ```
    cat input.txt | python mapper.py | sort | python reducer.py
    ```

### 5. **Reduce Step Fails**
- **Issue:** Parsing errors, empty lines, or unexpected input.
- **Fix:**  
  - Add error handling in reducer.
  - Skip empty or malformed lines.

---

## Summary

This exercise demonstrates how to use Hadoop and Cloudera for distributed data processing with Python MapReduce. You learned:
- How to set up input data and scripts.
- How to run jobs for wordcount, bigram count, and coolest year.
- How to troubleshoot common issues.

**Experiment with different data and logic to explore Hadoop’s power!**### 5. **Reduce Step Fails**
- **Issue:** Parsing errors, empty lines, or unexpected input.
- **Fix:**  
  - Add error handling in reducer.
  - Skip empty or malformed lines.

---

## Summary

This exercise demonstrates how to use Hadoop and Cloudera for distributed data processing with Python MapReduce. You learned:
- How to set up input data and scripts.
- How to run jobs for wordcount, bigram count, and coolest year.
- How to troubleshoot common issues.

**Experiment with different data and logic to explore Hadoop’s power!**