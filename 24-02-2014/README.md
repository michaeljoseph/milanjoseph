# Python Programming: Variables

## Setup

Launch the terminal and type in the following commands:

```bash
cd ~
mkdir -p code
cd code
touch variables.py
open variables.py
```

## Lesson 1: Variables and Functions

In your text editor, write code to meet the requirements below.
Save your work often and test your program by running this from the terminal:
python variables.py

1. Create a variable called `milan` and assign it the value of
   Milan Vincent Joseph's age as an integer.

1. Create a variable called `my_message` with the following contents:
   "Programming In Python Is Easy!" and use the `print` function to
   print `my_message` to the screen.

1. Type in these helper functions at the top of your program:

```python
from datetime import datetime


def ask(question):
    """Asks the user a question and returns their answer"""
    return raw_input('%s ' % question)


def this_year():
    """Returns the current year as an integer"""
    return datetime.now().year
```

#variables #`print` #functions

