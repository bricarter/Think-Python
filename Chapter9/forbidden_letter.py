"""
#GOAL:
# Create a function avoids()
# Parameters: word, string of letters
# Returns true if the word does not have any of the letters in it
# Write a program that prompts the user for input of  forbidden letters
# Read through words.txt
# Print the number of words that does not have any of the letters in it

#TODO:
# CREATE FUNCTION 
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""

def avoids(word, letters):
  for letter in letters:
    if letter in word: 
      return False
  return True


# MAIN
letters = input('Insert forbidden letters: ')

fin = open('words.txt')
line = fin.readline()

not_forbidden_count = 0
for line in fin:
  word = line.strip()
  if avoids(word, letters):
    not_forbidden_count += 1

print("Number of words not forbidden:", not_forbidden_count)
