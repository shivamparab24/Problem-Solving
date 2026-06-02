"""
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table. Each row of this table indicates the name of an employee, their department, and the id of their manager. If managerId is null, then the employee does not have a manager. No employee will be the manager of themself.

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: Employee table:

+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | None      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output:

+------+
| name |
+------+
| John |
+------+
"""


from pyspark.sql import functions as F
from pyspark.sql.types import *

from spark_session import get_spark

spark = get_spark("570")

data = [
    (101, "John",  "A", None),
    (102, "Dan",   "A", 101),
    (103, "James", "A", 101),
    (104, "Amy",   "A", 101),
    (105, "Anne",  "A", 101),
    (106, "Ron",   "B", 101)
]

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("department", StringType(), False),
    StructField("managerId", IntegerType(), True)
])

employee_df = spark.createDataFrame(data, schema)
employee_df.show()

#transformations

# result_df = employee_df.select('name').filter(F.col('id').isin(
#         list(employee_df.select('managerId').groupBy('managerId').agg(F.count(F.col('managerId')).alias('count')).filter(
#         F.col('count') >= 5).select('managerId').rdd.map(lambda x:x[0]).collect())
# ))



manager_counts = employee_df.groupBy("managerId").count().filter(F.col("count") >= 5)

result_df = employee_df.join(
    manager_counts,
    employee_df.id == manager_counts.managerId,
    "inner"
).select(employee_df.name)


result_df.show()