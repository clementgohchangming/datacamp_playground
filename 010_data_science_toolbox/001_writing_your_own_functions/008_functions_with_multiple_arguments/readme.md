# Functions that return multiple values
In the previous exercise, you constructed tuples, assigned tuples to variables, and unpacked tuples. Here you will return multiple values from a function using tuples. Let's now update our shout() function to return multiple values. Instead of returning just one string, we will return two strings with the string !!! concatenated to each.

Note that the return statement return x, y has the same result as return (x, y): the former actually packs x and y into a tuple under the hood!

# Instructions
- Modify the function header such that the function name is now shout_all, and it accepts two parameters, word1 and word2, in that order.
- Concatenate the string '!!!' to each of word1 and word2 and assign to shout1 and shout2, respectively.
- Construct a tuple shout_words, composed of shout1 and shout2.
- Call shout_all() with the strings 'congratulations' and 'you' and assign the result to yell1 and yell2 (remember, shout_all() returns 2 variables!).
