# Iterators as function arguments
You've been using the iter() function to get an iterator object, as well as the next() function to retrieve the values one by one from the iterator object.

There are also functions that take iterators and iterables as arguments. For example, the list() and sum() functions return a list and the sum of elements, respectively.

In this exercise, you will use these functions by passing an iterable from range() and then printing the results of the function calls.

# Instructions
- Create a range object that would produce the values from 10 to 20 using range(). Assign the result to values.
- Use the list() function to create a list of values from the range object values. Assign the result to values_list.
- Use the sum() function to get the sum of the values from 10 to 20 from the range object values. Assign the result to values_sum.
