# Python Programming: Input, Output and Calculations

## Lesson 2: Asking questions and doing maths

### Background: String interpolation

In Python, we can add strings together:

```python
name = 'Milan'
surname = 'Joseph'
full_name = name + surname
print(full_name)
```

We can also use string interpolation to achieve the same effect:

```python
full_name_with_a_space = '%s %s' % (name, surname)
print(full_name_with_a_space)
```

### Exercise

Using the helper functions `ask` and `this_year`, write code to do the following:

1. Ask the user for their name and store the value in a variable: `name`

1. Ask the user what year they were born and store it in `yob`

1. Ask the user whether they are male or female and store it in `gender`

1. Write some code to print out the following message using the variables:

```
Hello <name>!
It's nice to meet you :)
I'm Milan's first computer program in Python.
By my calculations, you are <age> Solar Lunar Cycles old.
And you are a <gender>
```
