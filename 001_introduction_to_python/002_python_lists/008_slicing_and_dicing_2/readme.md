# Slicing and dicing (2)
In the video, Hugo first discussed the syntax where you specify both where to begin and end the slice of your list:

```python
my_list[begin:end]
```

However, it's also possible not to specify these indexes. If you don't specify the begin index, Python figures out that you want to start your slice at the beginning of your list. If you don't specify the end index, the slice will go all the way to the last element of your list. To experiment with this, try the following commands in the IPython Shell:

```python
x = ["a", "b", "c", "d"]
x[:2]
x[2:]
x[:]
```

# Instructions
- Create `downstairs` again, as the first 6 elements of areas. This time, simplify the slicing by omitting the begin index.
- Create `upstairs` again, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.
