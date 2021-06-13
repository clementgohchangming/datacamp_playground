# Performing an anti-join
In our music streaming company dataset, each customer is assigned an employee representative to assist them. In this exercise, filter the employee table by a table of top customers, returning only those employees who are not assigned to a customer. The results should resemble the results of an anti-join. The company's leadership will assign these employees additional training so that they can work with high valued customers.

The top_cust and employees tables have been provided for you.

# Instructions

# Part 1
Merge employees and top_cust with a left join, setting indicator argument to True. Save the result to empl_cust.

# Part 2
Select the srid column of empl_cust and the rows where _merge_ is 'left_only'. Save the result to srid_list.

# Part 3
Subset the employees table and select those rows where the srid is in the variable srid_list and print the results.

