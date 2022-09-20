"""
GOAL:
# Create a function rotate_word()
# Parameters: string, int
# Returns a new string of the original string rotated by the int value
# Use ord() which converts a char to a numeric code
# Use chr() which converts a numeric code to a char
# Wrap z to a and Z to A

TODO:
# CREATE FUNCTION 
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""

def rotate_word(word, number):
 i = 0
 rotate = number % 26
 rotated = ''
 while i < len(word):
  if word[i].islower():
    rotated += chr(((ord(word[i]) - 97 + rotate) % 26) + 97)
    i += 1
  elif word[i].isupper():
    rotated += chr(((ord(word[i]) - 65 + rotate) % 26) + 65)
    i += 1
  else:
   rotated += word[i]
 return rotated
