# Computing percentage growth of GDP
Your job in this exercise is to compute the yearly percent-change of US GDP (Gross Domestic Product) since 2008.

The data has been obtained from the Federal Reserve Bank of St. Louis and is available in the file GDP.csv, which contains quarterly data; you will resample it to annual sampling and then compute the annual growth of GDP. For a refresher on resampling, check out the relevant material from pandas Foundations.

# Instructions
- Read the file 'GDP.csv' into a DataFrame called gdp, using parse_dates=True and index_col='DATE'.
- Create a DataFrame post2008 by slicing gdp such that it comprises all rows from 2008 onward.
- Print the last 8 rows of the slice post2008. This has been done for you. This data has quarterly frequency so the indices are separated by three-month intervals.
- Create the DataFrame yearly by resampling the slice post2008 by year. Remember, you need to chain .resample() (using the alias 'A' for annual frequency) with some kind of aggregation; you will use the aggregation method .last() to select the last element when resampling.
- Compute the percentage growth of the resampled DataFrame yearly with .pct_change() * 100.
