"""
GOAL:
# Copy example into a script + test it
# Modify do_twice
# Parameters: function, value
# Calls the function twice using the value as a parameter
# Copy print_twice function
# Call print_twice in do_twice
# Create a function do_four
# Parameters: function, value
# Calls the function four times using the value as a parameter
# There should only be two statements in the function body

TODO:
#DEFINE FUNCTION
#SET PARAMETERS
#SET RETURN TYPE
#SET RETURN VALUE
"""

def do_four(f, value):
 do_twice(f, value)
 do_twice(f, value)

def do_twice(f, value):
 f(value)
 f(value)

#def print_spam():
# print("spam")

def print_twice(bruce):
 print(bruce)
 print(bruce)

# MAIN  
do_twice(print_twice, 'SPAM')
do_four(print_twice, 'spam')
