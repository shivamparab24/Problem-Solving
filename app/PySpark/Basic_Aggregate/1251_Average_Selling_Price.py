"""
Table: Prices

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table. Each row of this table indicates the price of the product_id in the period from start_date to end_date. For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.

Table: UnitsSold

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows. Each row of this table indicates the date, units, and product_id of each product sold.

Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: Prices table:

+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+
UnitsSold table:

+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+
Output:

+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+
Explanation: Average selling price = Total Price of Product / Number of products sold. Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96 Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96
"""


from datetime import date

from pyspark.sql import functions as F
from pyspark.sql.types import *

from spark_session import get_spark

spark = get_spark("1251")


prices_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("start_date", DateType(), False),
    StructField("end_date", DateType(), False),
    StructField("price", IntegerType(), False)
])

prices_data = [
    (1, date(2019, 2, 17), date(2019, 2, 28), 5),
    (1, date(2019, 3, 1),  date(2019, 3, 22), 20),
    (2, date(2019, 2, 1),  date(2019, 2, 20), 15),
    (2, date(2019, 2, 21), date(2019, 3, 31), 30)
]

prices_df = spark.createDataFrame(prices_data, schema=prices_schema)

units_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("purchase_date", DateType(), False),
    StructField("units", IntegerType(), False)
])

units_data = [
    (1, date(2019, 2, 25), 100),
    (1, date(2019, 3, 1), 15),
    (2, date(2019, 2, 10), 200),
    (2, date(2019, 3, 22), 30)
]

units_df = spark.createDataFrame(units_data, schema=units_schema)


prices_df.show()
units_df.show()


results_df = prices_df.alias('a').join(units_df,
                            on = (prices_df["product_id"] == units_df["product_id"])
                                & ((prices_df['start_date'] <= units_df['purchase_date'])
                                    & (prices_df['end_date'] >= units_df['purchase_date'])),
                            how = 'inner') \
                        .groupBy('a.product_id') \
                        .agg(F.round(F.sum(F.col('price') * F.col('units')) / F.sum('units'), 2).alias('average_price'))

results_df.show()

