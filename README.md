# Sample pyspark example
Sample code for reading odds history from data.oddsmagnet.com

There are two pathes available to read from:

- data.oddsmagnet.com/history-daily/
- data.oddsmagnet.com/history/

At the first location you will find daily aggregated data, where one row represents aggregated average of odds among all bookmaker for a day. The other location has a ___sample___ of data, which you can find in a paid version of odds history. At the second location one row represents one change per individual bookmaker with timestamp.

Both locations have data in PARQUET format with SNAPPY compression partirioned by ingest_year, ingest_month, ingest_day.

Daily data get aggregated once a day at 22:00 UK time. 

