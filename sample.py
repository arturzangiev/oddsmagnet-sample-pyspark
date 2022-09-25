from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession.builder\
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.2.0')\
        .config(
            'spark.hadoop.fs.s3a.aws.credentials.provider', 
            'org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider'
        ).getOrCreate()
  
    # df = spark.read.parquet("s3a://data.oddsmagnet.com/history-daily/")
    df = spark.read.parquet("s3a://data.oddsmagnet.com/history/")
    df.printSchema()
    df.show()