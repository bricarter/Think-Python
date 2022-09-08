"""
GOAL:
# Create a function is_triangle()
# Parameters: three ints
# If side1 + side2 > side3 print 'Yes', else print 'No'
# Create a function that ask for user input for the sides
# Convert the input into ints 
# Calls check_fermat() to check whether the values form a triangle

TODO:
# TEST FORMULA

# CREATE FUNCTION 
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""

def check_fermat(side_one, side_two, side_three):
 if (side_one + side_two) > side_three:
  print('Yes')
 else:
  print('No')

def sides_user_input():
 side_one = input('Insert a positive value for side one:\n')
 side_two = input('Insert a positive value for side two:\n')
 side_three = input('Insert a positive value for side three:\n')
 check_fermat(int(side_one), int(side_two), int(side_three))
