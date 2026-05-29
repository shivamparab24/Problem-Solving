"""
Table: Cinema

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key (column with unique values) for this table. Each row contains information about the name of a movie, its genre, and its rating. rating is a 2 decimal places float in the range [0, 10]

Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.

The result format is in the following example.

Example 1:

Input: Cinema table:

+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+
Output:

+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
+----+------------+-------------+--------+
Explanation: We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.
"""


from pyspark.sql import functions as F
from pyspark.sql.types import *

from spark_session import get_spark

spark = get_spark()

data = [
    [1, 'War', 'great 3D', 8.9],
    [2, 'Science', 'fiction', 8.5],
    [3, 'irish', 'boring', 6.2],
    [4, 'Ice song', 'Fantacy', 8.6],
    [5, 'House card', 'Interesting', 9.1]
]

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("movie", StringType(), True),
    StructField("description", StringType(), True),
    StructField("rating", FloatType(), True)
])

cinema_df = spark.createDataFrame(data, schema)
cinema_df.show()

#transfomrations 

result_df = cinema_df.filter(
    (F.col('id') % 2 != 0) & (F.col('description') != 'boring')
).orderBy(F.col('rating').desc())

result_df.show()