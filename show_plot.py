#!/usr/bin/env python3
import PIL.Image
from pyhive import hive
import pandas as pd
import matplotlib.pyplot as plt

cursor = hive.connect('localhost')
select = """SELECT latitude, longitude, price FROM airbnb
            WHERE neighbourhood = 'Westminster' AND
            room_type <> 'Private room' AND
            room_type <> 'Shared room' AND
            minimum_nights <= 2 AND
            number_of_reviews > 2 AND
            number_of_reviews > 20
            ORDER BY price LIMIT 10"""

buckingham_latitude = 51.501476
buckingham_longitude = -0.140634


london_airbnb = pd.read_sql(select,cursor)
print(london_airbnb)

BBox = (-0.2077,-0.0944, 51.4772, 51.5230)
ruh_m = plt.imread(r'/home/hadoop/airbnb/london.png')

fig, ax = plt.subplots(figsize = (20,18))
ax.scatter(london_airbnb.longitude, london_airbnb.latitude, zorder=1, alpha= 1, c='b', s=1000)
ax.set_title('London airbnb stays')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
plt.savefig(r"/home/hadoop/airbnb/test2.png")
im = PIL.Image.open(r"/home/hadoop/airbnb/test2.png")
im.show()

windowSpec = Window.partitionBy("name").orderBy("year")

salaryHistory.withColumn("rank", f.lag(f.col("salary")).over(windowSpec))\
             .withColumn("diff", f.col("salary") - f.col("year").over(windowSpec)).show(30)

salaryHistory.withColumn("rank", f.rank().over(windowSpec))\
             .withColumn("dense_rank", f.dense_rank().over(windowSpec))\
             .withColumn("row_num", f.row_number().over(windowSpec)).show(30)