#!/usr/bin/env python3

from pyhive import hive
cursor = hive.connect('localhost').cursor()
#nsert = "CREATE EXTERNAL TABLE IF NOT EXISTS movies (movieID INT, title STRING, genres STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '@'"
insert = """CREATE EXTERNAL TABLE IF NOT EXISTS airbnb
            (
            id INT,
            name STRING,
            host_id STRING,
            host_name STRING,
            neighbourhood_group STRING,
            neighbourhood STRING,
            latitude FLOAT,
            longitude FLOAT,
            room_type STRING,
            price INT,
            minimum_nights INT,
            number_of_reviews INT,
            last_review DATE,
            reviews_per_month FLOAT,
            calculated_host_listings_count INT,
            availability_365 INT,
            number_of_reviews_ltm INT,
            license STRING
            )
            ROW FORMAT DELIMITED
            FIELDS TERMINATED BY ','"""
cursor.execute(insert)

insert2 = """LOAD DATA LOCAL INPATH '/home/hadoop/airbnb/listings.csv'
             OVERWRITE INTO TABLE airbnb"""
cursor.execute(insert2)
