# Ticks
zThe customizations you've coded up to now are available in the script, in a more concise form.

In the video, Hugo has demonstrated how you could control the y-ticks by specifying two arguments:

```python
plt.yticks([0,1,2], ["one","two","three"])
```

In this example, the ticks corresponding to the numbers 0, 1 and 2 will be replaced by one, two and three, respectively.

Let's do a similar thing for the x-axis of your world development chart, with the `xticks()` function. The tick values `1000`, `10000` and `100000` should be replaced by `1k`, `10k` and `100k`. To this end, two lists have already been created for you: `tick_val` and `tick_lab`.

# Instructions

- Use `tick_val` and `tick_lab` as inputs to the `xticks()` function to make the the plot more readable.
- As usual, display the plot with `plt.show()` after you've added the customizations.
