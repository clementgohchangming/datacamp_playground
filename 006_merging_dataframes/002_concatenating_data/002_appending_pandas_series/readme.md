# Appending pandas Series
In this exercise, you'll load sales data from the months January, February, and March into DataFrames. Then, you'll extract Series with the 'Units' column from each and append them together with method chaining using .append().

To check that the stacking worked, you'll print slices from these Series, and finally, you'll add the result to figure out the total units sold in the first quarter.

# Instructions
- Read the files 'sales-jan-2015.csv', 'sales-feb-2015.csv' and 'sales-mar-2015.csv' into the DataFrames jan, feb, and mar respectively.
- Use parse_dates=True and index_col='Date'.
- Extract the 'Units' column of jan, feb, and mar to create the Series jan_units, feb_units, and mar_units respectively.
- Construct the Series quarter1 by appending feb_units to jan_units and then appending mar_units to the result. Use chained calls to the .append() method to do this.
- Verify that quarter1 has the individual Series stacked vertically. To do this:
- Print the slice containing rows from jan 27, 2015 to feb 2, 2015.
- Print the slice containing rows from feb 26, 2015 to mar 7, 2015.
- Compute and print the total number of units sold from the Series quarter1. This has been done for you, so hit 'Submit Answer' to see the result!

