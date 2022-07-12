This project used free-accessible data from airbnb regarding accommodation offers in London on this portal.
Data can be donloaded from this link: http://data.insideairbnb.com/united-kingdom/england/london/2021-12-07/visualisations/listings.csv

Project is supposed to run on EMR on AWS with use of Hive database to store airbnb data in one of previously defined table.
Thanks to Hive SQL query accommodations are filtered to ones located in Westminister district of London.
Also results of the query are sorted descendingly by price per night and only top 10 results are taken into consideration.

FInally - thanks to matplotlib library - user can see map with centre of London with results of the cheapest stays in Westminister.
Please see this data visualation concept opening test2,png file.

This project has been made after a short-trip to London ;-)

