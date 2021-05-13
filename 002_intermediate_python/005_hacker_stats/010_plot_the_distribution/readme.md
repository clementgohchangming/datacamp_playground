# Plot the distribution
All these fancy visualizations have put us on a sidetrack. We still have to solve the million-dollar problem: What are the odds that you'll reach 60 steps high on the Empire State Building?

Basically, you want to know about the end points of all the random walks you've simulated. These end points have a certain distribution that you can visualize with a histogram.

Note that if your code is taking too long to run, you might be plotting a histogram of the wrong data!

# Instructions
- To make sure we've got enough simulations, go crazy. Simulate the random walk 500 times.
- From np_aw_t, select the last row. This contains the endpoint of all 500 random walks you've simulated. Store this Numpy array as ends.
- Use plt.hist() to build a histogram of ends. Don't forget plt.show() to display the plot.
