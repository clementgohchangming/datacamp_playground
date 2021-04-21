# Sizes
Right now, the scatter plot is just a cloud of blue dots, indistinguishable from each other. Let's change this. Wouldn't it be nice if the size of the dots corresponds to the population?

To accomplish this, there is a list `pop` loaded in your workspace. It contains population numbers for each country expressed in millions. You can see that this list is added to the scatter method, as the argument `s`, for size.

# Instructions
- Run the script to see how the plot changes.
- Looks good, but increasing the size of the bubbles will make things stand out more.
- Import the `numpy` package as `np`.
- Use `np.array()` to create a numpy array from the list `pop`. Call this Numpy array `np_pop`.
- Double the values in n`p_pop` setting the value of np_p`op` equal to `np_pop * 2`. Because `np_pop` is a Numpy array, each array element will be doubled.
Change the s argument inside `plt.scatter()` to be `np_pop` instead of `pop`.
