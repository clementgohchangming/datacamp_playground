# Baseball player's BMI
The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: `height_in` and `weight_lb`. `height_in` is in inches and `weight_lb` is in pounds.

It's now possible to calculate the BMI of each baseball player. Python code to convert `height_in` to a `numpy` array with the correct units is already available in the workspace. Follow the instructions step by step and finish the game!

# Instructions
- Create a `numpy` array from the `weight_lb` list with the correct units. Multiply by `0.453592` to go from pounds to kilograms. Store the resulting `numpy` array as `np_weight_kg`.
- Use `np_height_m` and `np_weight_kg` to calculate the BMI of each player. Use the following equation:
```python
bmi = np_height_m / np_weight_kg**2
```
Save the resultant `numpy` array as `bmi`.
- Print out `bmi`


