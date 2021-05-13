# Implement clumsiness
With this neatly written code of yours, changing the number of times the random walk should be simulated is super-easy. You simply update the range() function in the top-level for loop.

There's still something we forgot! You're a bit clumsy and you have a 0.1% chance of falling down. That calls for another random number generation. Basically, you can generate a random float between 0 and 1. If this value is less than or equal to 0.001, you should reset step to 0.

# Instructions
- Change the range() function so that the simulation is performed 250 times.
- Finish the if condition so that step is set to 0 if a random float is less or equal to 0.001. Use np.random.rand().

