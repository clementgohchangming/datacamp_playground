# Subsetting NumPy Arrays
You've seen it with your own eyes: Python lists and `numpy` arrays sometimes behave differently. Luckily, there are still certainties in this world. For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same. To see this for yourself, try the following lines of code in the IPython Shell:

```python
x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]
```

The script in the editor already contains code that imports `numpy` as `np`, and stores both the height and weight of the MLB players as `numpy` arrays.

# Instructions
- Subset np_weight_lb by printing out the element at index 50.
- Print out a sub-array of np_height_in that contains the elements at index 100 up to and including index 110.
