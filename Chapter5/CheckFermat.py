"""
GOAL:
# Create a function check_fermat()
# Paramters: a, b, c, n
# Use formula
# If n > 2 and the formula returns true, print 'Holy smokes, Fermat was wrong!'
# Else print 'No, that doesn't work.'
# Create a function that prompts a user for input 
# Convert and store input into values a, b, c, n
# Call check_fermat() to check the variables against the formula

TODO:
# TEST FORMULA

# CREATE FUNCTION 
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""

def check_fermat(a, b, c, n):
 if n > 2 and (a**n + b**n) == c**n:
  print('Holy smokes, Fermat was wrong!')
 else:
  print("No, that doesn't work.")

def user_input():
 a = input('Insert a positive value for variable a:\n')
 b = input('Insert a positive value for variable b:\n')
 c = input('Insert a positive value for variable b:\n')
 n = input('Insert a positive exponent value:\n')
 check_fermat(int(a), int(b), int(c), int(n))
