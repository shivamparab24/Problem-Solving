"""Table: World

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table. Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or it has a population of at least twenty-five million (i.e., 25000000). Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: World table:

+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output:

+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+"""



from spark_session import get_spark
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, LongType

spark = get_spark("595_bc")


data = [
    ['Afghanistan', 'Asia', 652230, 25500100, 20343000000],
    ['Albania', 'Europe', 28748, 2831741, 12960000000],
    ['Algeria', 'Africa', 2381741, 37100000, 188681000000],
    ['Andorra', 'Europe', 468, 78115, 3712000000],
    ['Angola', 'Africa', 1246700, 20609294, 100990000000]

]

schema = StructType([
    StructField("name", StringType(), True),
    StructField("continent", StringType(), True),
    StructField("area", LongType(), True),
    StructField("population", LongType(), True),
    StructField("gdp", LongType(), True)
])

countries_df = spark.createDataFrame(data = data, schema = schema)

countries_df.show()


#transformations
result = countries_df.filter(
    (F.col("area") >= 3000000) | (F.col("population") >= 25000000)
)

result.select("name", "population", "area").show()