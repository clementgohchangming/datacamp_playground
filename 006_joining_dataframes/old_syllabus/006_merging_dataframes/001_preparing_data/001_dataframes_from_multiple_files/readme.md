# Reading DataFrames from multiple files
When data is spread among several files, you usually invoke pandas' read_csv() (or a similar data import function) multiple times to load the data into several DataFrames.

The data files for this example have been derived from a list of Olympic medals awarded between 1896 & 2008 compiled by the Guardian.

The column labels of each DataFrame are NOC, Country, & Total where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won (bronze, silver, or gold).

This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the Pandas Cheat Sheet and keep it handy!

# Instructions
- Import pandas as pd.
- Read the file 'Bronze.csv' into a DataFrame called bronze.
- Read the file 'Silver.csv' into a DataFrame called silver.
- Read the file 'Gold.csv' into a DataFrame called gold.
- Print the first 5 rows of the DataFrame gold. This has been done for you, so hit 'Submit Answer' to see the results.
