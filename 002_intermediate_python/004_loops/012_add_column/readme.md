# Add column (1)
In the video, Hugo showed you how to add the length of the country names of the brics DataFrame in a new column:
```python
for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])
```
You can do similar things on the cars DataFrame.

# Instructions
- Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. You can use the string method upper() for this.
- To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.
