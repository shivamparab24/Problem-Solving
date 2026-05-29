"""Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table. The table has information about incoming transactions. The state column is an enum of type ("approved", "declined").

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input: Transactions table:

+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
Output:

+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
"""


from pyspark.sql import functions as F
from pyspark.sql.types import *
from datetime import date

from spark_session import get_spark

spark = get_spark("1193")


schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("country", StringType(), True),
    StructField("state", StringType(), True),
    StructField("amount", IntegerType(), True),
    StructField("trans_date", DateType(), True)
])

data = [
    (121, "US", "approved", 1000, date(2018, 12, 18)),
    (122, "US", "declined", 2000, date(2018, 12, 19)),
    (123, "US", "approved", 2000, date(2019, 1, 1)),
    (124, "DE", "approved", 2000, date(2019, 1, 7))
]

transactions_df = spark.createDataFrame(data, schema)
transactions_df.show()


#transformations

# results_df = transactions_df.withColumn('month', F.substring('trans_date', 0, 7)) \
#     .groupBy('month', 'country') \
#     .agg(
#         F.count('id').alias('trans_count'),
#         F.sum(F.when(F.col('state') == 'approved', 1).otherwise(0)).alias('approved_count'),
#         F.sum('amount').alias('trans_total_amount'),
#         F.sum(F.when(F.col('state') == 'approved', F.col('amount')).otherwise(0).alias('approved_total_amount'))
#     )

results_df = (
    transactions_df
    .withColumn('month', F.date_format('trans_date', 'yyyy-MM'))
    .groupBy('month', 'country')
    .agg(
        F.count('id').alias('trans_count'),
        F.sum(F.when(F.col('state') == 'approved', 1).otherwise(0)).alias('approved_count'),
        F.sum('amount').alias('trans_total_amount'),
        F.sum(
            F.when(F.col('state') == 'approved', F.col('amount')).otherwise(0)
        ).alias('approved_total_amount')
    )
)

results_df.show()