# Your first inner join
You have been tasked with figuring out what the most popular types of fuel used in Chicago taxis are. To complete the analysis, you need to merge the taxi_owners and taxi_veh tables together on the vid column. You can then use the merged table along with the .value_counts() method to find the most common fuel_type.

Since you'll be working with pandas throughout the course, the package will be preloaded for you as pd in each exercise in this course. Also the taxi_owners and taxi_veh DataFrames are loaded for you.

# Instructions

# Part 1
Merge taxi_owners with taxi_veh on the column vid, and save the result to taxi_own_veh.

# Part 2
Set the left and right table suffixes for overlapping columns of the merge to _own and _veh_, respectively.

# Part 3
Select the fuel_type column from taxi_own_veh and print the value_counts() to find the most popular fuel_types used.
