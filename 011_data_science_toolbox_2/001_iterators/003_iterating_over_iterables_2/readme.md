# Iterating over iterables (2)
One of the things you learned about in this chapter is that not all iterables are actual lists. A couple of examples that we looked at are strings and the use of the range() function. In this exercise, we will focus on the range() function.

You can use range() in a for loop as if it's a list to be iterated over:

for i in range(5):
    print(i)
Recall that range() doesn't actually create the list; instead, it creates a range object with an iterator that produces the values until it reaches the limit (in the example, until the value 4). If range() created the actual list, calling it with a value of  may not work, especially since a number as big as that may go over a regular computer's memory. The value  is actually what's called a Googol which is a 1 followed by a hundred 0s. That's a huge number!

Your task for this exercise is to show that calling range() with  won't actually pre-create the list.

# Instructions
- Create an iterator object small_value over range(3) using the function iter().
- Using a for loop, iterate over range(3), printing the value for every iteration. Use num as the loop variable.
- Create an iterator object googol over range(10 ** 100).
