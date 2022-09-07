"""
GOAL:
# Create a function gcd()
# Parameters: a, b
# Returns their greatest common divisor
# gcd(a, b) == gcd(r, b) 
# gcd(a, 0) == a

TODO:
# SET BASE CASE
# PRINT BASE
# CREATE RECURSION
# PRINT RECURSION
"""

def gcd(a, b):
  print(a,b)
  if b == 0:
    return a
  else:
    r = a % b
    return gcd(b, r)
