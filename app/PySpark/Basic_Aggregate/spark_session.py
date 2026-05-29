from pyspark.sql import SparkSession


def get_spark(app_name: str = "spark_app") -> SparkSession:
    """
    Create or get an existing SparkSession.

    Args:
        app_name (str): Name of the Spark application

    Returns:
        SparkSession
    """

    spark = (
        SparkSession.builder
        .appName(app_name)
        .getOrCreate()
    )

    return spark