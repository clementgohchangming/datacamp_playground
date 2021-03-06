# Slicing time series
Slicing is particularly useful for time series since it's a common thing to want to filter for data within a date range. Add the date column to the index, then use .loc[] to perform the subsetting. The important thing to remember is to keep your dates in ISO 8601 format, that is, yyyy-mm-dd.

Recall from Chapter 1 that you can combine multiple Boolean conditions using logical operators (such as &). To do so in one line of code, you'll need to add parentheses () around each condition.

pandas is loaded as pd and temperatures, with no index, is available.Pivot for mean weekly_sales by store type and holiday 

# Instructions
-Use Boolean conditions (not .isin() or .loc[]) to subset for rows in 2010 and 2011, and print the results.
-Note that because the date isn't set as an index, a condition that contains only a year, such as df["date"] == "2009", will check if the date is equal to the first day of the first month of the year (e.g. 2009-01-01), rather than checking whether the date occurs within the given year. We recommend writing out the full date when using Boolean conditions (e.g., 2009-12-31).
-Set the index to the date column.
-Use .loc[] to subset for rows in 2010 and 2011.
-Use .loc[] to subset for rows from Aug 2010 to Feb 2011.
