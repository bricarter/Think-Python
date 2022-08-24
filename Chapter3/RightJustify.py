"""
GOAL:
# Create a function right_justify()
# Parameters: string s
# Prints the string with leading spaces that places the last letter of the string in column 70 of the display
# Use string concatenation, repetition, and len() function

TODO:
# DEFINE FUNCTION
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""
 
def right_justify(s):
 whitespace = 70 - len(s)
 print(" "*whitespace + s)
