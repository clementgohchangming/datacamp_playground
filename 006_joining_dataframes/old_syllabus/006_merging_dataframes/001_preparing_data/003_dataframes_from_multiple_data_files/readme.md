# Combining DataFrames from multiple data files
In this exercise, you'll combine the three DataFrames from earlier exercises - gold, silver, & bronze - into a single DataFrame called medals. The approach you'll use here is clumsy. Later on in the course, you'll see various powerful methods that are frequently used in practice for concatenating or merging DataFrames.

Remember, the column labels of each DataFrame are NOC, Country, and Total, where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won.

# Instructions
- Construct a copy of the DataFrame gold called medals using the .copy() method.
- Create a list called new_labels with entries 'NOC', 'Country', & 'Gold'. This is the same as the column labels from gold with the column label 'Total' replaced by 'Gold'.
- Rename the columns of medals by assigning new_labels to medals.columns.
- Create new columns 'Silver' and 'Bronze' in medals using silver['Total'] & bronze['Total'].
- Print the top 5 rows of the final DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!
