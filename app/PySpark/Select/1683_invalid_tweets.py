"""Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table. This table contains all the tweets in a social media app.

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: Tweets table:

+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+
Output:

+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation: Tweet 1 has length = 14. It is a valid tweet. Tweet 2 has length = 32. It is an invalid tweet."""



from pyspark.sql.types import *
from pyspark.sql import functions as F
from spark_session import get_spark

spark = get_spark("1683")

data = [
    [1, "Vote for Biden"],
    [2, "Let us make America great again"]
]

schema = StructType([
    StructField("tweet_id", IntegerType(), True),
    StructField("content", StringType(), True)
])


tweets_df = spark.createDataFrame(data, schema)

tweets_df.show()

result_df = tweets_df.filter(
    (F.length(F.col("content"))>15)
).select("tweet_id")

result_df.show()
