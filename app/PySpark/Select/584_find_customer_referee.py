"""Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table. Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: Customer table:

+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output:

 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+"""




from pyspark.sql import functions as F
from spark_session import get_spark

spark = get_spark("584_fcr")


data = [
    [1, "Will", None],
    [2, "Jane", None],
    [3, "Alex", 2],
    [4, "Bill", None],
    [5, "Zack", 1],
    [6, "Mark", 2]
]

columns = ["id", "name", "referee_id"]

customer_df = spark.createDataFrame(data, columns)
customer_df.show(truncate=False)

# transformation

result_df = customer_df.filter(
    (
        (F.col('referee_id').isNull()) | (F.col('referee_id') != 2)
    )
)

result_df.select("name").show(truncate=False)

