import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

def main():

    spark = (
        SparkSession.builder.appName("transform_sales")
        .master("local[*]")
        .config("spark.python.worker.faulthandler.enabled", "true")
        .getOrCreate()
    )

    data = [(1, 100), (2, 200), (3, 300)]

    df = spark.createDataFrame(data, ["id", "amount"])

    df2 = df.withColumn("amount_doubled", col("amount") * 2)

    df2.show()

    spark.stop()


if __name__ == "__main__":
    main()
