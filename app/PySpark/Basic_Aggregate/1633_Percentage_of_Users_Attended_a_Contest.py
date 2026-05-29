"""Table: Users

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| user_name   | varchar |
+-------------+---------+
user_id is the primary key (column with unique values) for this table. Each row of this table contains the name and the id of a user.

Table: Register

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| contest_id  | int     |
| user_id     | int     |
+-------------+---------+
(contest_id, user_id) is the primary key (combination of columns with unique values) for this table. Each row of this table contains the id of a user and the contest they registered into.

Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

The result format is in the following example.

Example 1:

Input: Users table:

+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6       | Alice     |
| 2       | Bob       |
| 7       | Alex      |
+---------+-----------+
Register table:

+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 7       |
| 209        | 6       |
| 215        | 7       |
| 208        | 7       |
| 210        | 2       |
| 207        | 2       |
| 210        | 7       |
+------------+---------+
Output:

+------------+------------+
| contest_id | percentage |
+------------+------------+
| 208        | 100.0      |
| 209        | 100.0      |
| 210        | 100.0      |
| 215        | 66.67      |
| 207        | 33.33      |
+------------+------------+
Explanation: All the users registered in contests 208, 209, and 210. The percentage is 100% and we sort them in the answer table by contest_id in ascending order. Alice and Alex registered in contest 215 and the percentage is ((2/3) * 100) = 66.67% Bob registered in contest 207 and the percentage is ((1/3) * 100) = 33.33%
"""

from pyspark.sql import functions as F
from pyspark.sql.types import *

from spark_session import get_spark

spark = get_spark("1633")


users_data = [
    (6, "Alice"),
    (2, "Bob"),
    (7, "Alex")
]

users_schema = StructType([
    StructField("user_id", IntegerType(), True),
    StructField("user_name", StringType(), True)
])

users_df = spark.createDataFrame(users_data, users_schema)


register_data = [
    (215, 6),
    (209, 2),
    (208, 2),
    (210, 6),
    (208, 6),
    (209, 7),
    (209, 6),
    (215, 7),
    (208, 7),
    (210, 2),
    (207, 2),
    (210, 7)
]

register_schema = StructType([
    StructField("contest_id", IntegerType(), True),
    StructField("user_id", IntegerType(), True)
])

register_df = spark.createDataFrame(register_data, register_schema)


users_df.show()
register_df.show()


#transformations

result_df = register_df\
        .join(users_df, on=['user_id'], how='inner')\
        .groupBy('contest_id').agg(F.count('user_id').alias('users_count'))\
        .withColumn('percentage', F.round(100*F.col('users_count')/users_df.count(), 2))\
        .drop('users_count')\
        .orderBy(F.col('percentage').desc(), 'contest_id')

result_df.show()