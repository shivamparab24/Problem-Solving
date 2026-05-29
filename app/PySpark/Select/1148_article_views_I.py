"""Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows. Each row of this table indicates that some viewer viewed an article (written by some author) on some date. Note that equal author_id and viewer_id indicate the same person.

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.

Example 1:

Input: Views table:

+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output:

+------+
| id   |
+------+
| 4    |
| 7    |
+------+"""


from pyspark.sql import functions as F
from spark_session import get_spark
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = get_spark("1148")

data = [
    [1, 3, 5, '2019-08-01'],
    [1, 3, 6, '2019-08-02'],
    [2, 7, 7, '2019-08-01'],
    [2, 7, 6, '2019-08-02'],
    [4, 7, 1, '2019-07-22'],
    [3, 4, 4, '2019-07-21'],
    [3, 4, 4, '2019-07-21']
]

schema = StructType([
    StructField("article_id", IntegerType(), True),
    StructField("author_id", IntegerType(), True),
    StructField("viewer_id", IntegerType(), True),
    StructField("view_date", StringType(), True)
])

article_df = spark.createDataFrame(data=data, schema=schema)

article_df.show()


#transformations

result_df = article_df.filter(
    (
        F.col("author_id") == F.col("viewer_id")
    )
).select(F.col("author_id").alias("id")).distinct().orderBy("id")

result_df.show()