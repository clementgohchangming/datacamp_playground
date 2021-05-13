# How low can you go?
Things are shaping up nicely! You already have code that calculates your location in the Empire State Building after 100 dice throws. However, there's something we haven't thought about - you can't go below 0!

A typical way to solve problems like this is by using max(). If you pass max() two arguments, the biggest one gets returned. For example, to make sure that a variable x never goes below 10 when you decrease it, you can use:
```python
x = max(10, x - 1)
```

# Instructions
- Use max() in a similar way to make sure that step doesn't go below zero if dice <= 2.
- Hit Submit Answer and check the contents of random_walk.
