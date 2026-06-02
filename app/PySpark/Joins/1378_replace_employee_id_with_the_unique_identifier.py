"""
Table: Employees

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table. Each row of this table contains the id and the name of an employee in a company.

Table: EmployeeUNI

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table. Each row of this table contains the id and the corresponding unique id of an employee in the company.

Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: Employees table:

+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:

+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
Output:

+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
Explanation: Alice and Bob do not have a unique ID, We will show null instead. The unique ID of Meir is 2. The unique ID of Winston is 3. The unique ID of Jonathan is 1.
"""


from pyspark.sql import functions as F
from pyspark.sql.types import *

from spark_session import get_spark

data1 = [
    [1, "Alice"],
    [7, "Bob"],
    [11, "Meir"],
    [90, "Winston"],
    [3, "Jonathan"]
]

schema1 = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)
])

spark = get_spark("1378")

emp_df = spark.createDataFrame(data1, schema1)
emp_df.show()


data2 = [
    [3, 1],
    [11, 2],
    [90, 3]
]

schema2 = StructType([
    StructField("id", IntegerType(), True),
    StructField("unique_id", IntegerType(), True)
])

empuni_df = spark.createDataFrame(data2, schema2)
empuni_df.show()
#transformations


result_df = emp_df.join(empuni_df, on=['id'], how='left').select("unique_id", "name")

result_df.show()