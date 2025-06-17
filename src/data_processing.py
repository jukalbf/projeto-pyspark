
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TransportePublico").getOrCreate()

df_sptrans = spark.read.csv("data/raw/sptrans_linhas.csv", header=True, inferSchema=False)
df_sptrans.printSchema()
df_sptrans.show(5)
