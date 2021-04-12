# Can Python handle everything?
Now that you know something more about combining different sources of information, have a look at the four Python expressions below. Which one of these will throw an error? You can always copy and paste this code in the IPython Shell to find out!

# Instructions

1. `"I can add integers, like " + str(5) + " to strings."`
2. `"I said " + ("Hey " * 2) + "Hey!"`
3. `"The correct answer to this multiple choice exercise is answer number " + 2`
4. `True + False`

# Answer

3. `"The correct answer to this multiple choice exercise is answer number " + 2`

# Console

```
In [1]:
 
"I can add integers, like " + str(5) + " to strings."
Out[1]:
'I can add integers, like 5 to strings.'
In [2]:
"I said " + ("Hey " * 2) + "Hey!"
Out[2]:
'I said Hey Hey Hey!'
In [3]:
"The correct answer to this multiple choice exercise is answer number " + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    "The correct answer to this multiple choice exercise is answer number " + 2
TypeError: must be str, not int
In [4]:
True + False
Out[4]:
1
```
