"""
GOAL:
# Copy functions
# Create a function is_palindrome()
# Parameters: a string
# Returns true or false
# Can use the built in function len()

TODO:
# SET BASE CASE
# CREATE RECURSION

"""

def first(word):
  return word[0]

def last(word):
  return word[-1]

def middle(word):
  return word[1:-1]

def is_palindrome(word): 
  if len(word) < 2:
    return True
  elif first(word) == last(word):
    return is_palindrome(middle(word))
  else:
    return False
