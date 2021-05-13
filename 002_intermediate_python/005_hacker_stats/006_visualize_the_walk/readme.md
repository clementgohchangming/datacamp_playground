# Visualize the walk
Let's visualize this random walk! Remember how you could use matplotlib to build a line plot?
```python
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
The first list you pass is mapped onto the x axis and the second list is mapped onto the y axis.
```
If you pass only one argument, Python will know what to do and will use the index of the list to map onto the x axis, and the values in the list onto the y axis.

# Instructions
Add some lines of code after the for loop:

- Import matplotlib.pyplot as plt.
- Use plt.plot() to plot random_walk.
- Finish off with plt.show() to actually display the plot.
