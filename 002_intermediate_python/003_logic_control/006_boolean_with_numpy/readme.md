# Boolean operators with Numpy
Before, the operational operators like < and >= worked with Numpy arrays out of the box. Unfortunately, this is not true for the boolean operators and, or, and not.

To use these operators with Numpy, you will need np.logical_and(), np.logical_or() and np.logical_not(). Here's an example on the my_house and your_house arrays from before to give you an idea:

```python
np.logical_and(my_house > 13, 
               your_house < 15)
```

# Instructions

- Generate boolean arrays that answer the following questions:
- Which areas in my_house are greater than 18.5 or smaller than 10?
- Which areas are smaller than 11 in both my_house and your_house? Make sure to wrap both commands in print() statement, so that you can inspect the output.
