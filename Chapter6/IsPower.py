"""
#GOAL:
# Create a function is_power()
# Parameters: a, b
# Returns true if a is a power of b, false if not
# a is a power of b if: a is divisible by b and a/b is a power of b

#TODO:
# SET BASE CASE
# PRINT BASE
# CREATE RECURSION
# PRINT RECURSION
"""

def is_power(a, b):
  if a / b == 1:
    return True
  if a % b != 0:
    return False
  return is_power(a/b, b)
