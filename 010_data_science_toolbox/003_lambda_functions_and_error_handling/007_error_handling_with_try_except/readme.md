# Error handling with try-except
A good practice in writing your own functions is also anticipating the ways in which other people (or yourself, if you accidentally misuse your own function) might use the function you defined.

As in the previous exercise, you saw that the len() function is able to handle input arguments such as strings, lists, and tuples, but not int type ones and raises an appropriate error and error message when it encounters invalid input arguments. One way of doing this is through exception handling with the try-except block.

In this exercise, you will define a function as well as use a try-except block for handling cases when incorrect input arguments are passed to the function.

Recall the shout_echo() function you defined in previous exercises; parts of the function definition are provided in the sample code. Your goal is to complete the exception handling code in the function definition and provide an appropriate error message when raising an error.

# Instructions
- Initialize the variables echo_word and shout_words to empty strings.
- Add the keywords try and except in the appropriate locations for the exception handling block.
- Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
- Concatenate the string '!!!' to echo_word. Assign the result to shout_words.
