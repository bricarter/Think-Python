"""
GOAL:
# Create a function has_no_e()
# Returns true if the word does not have an 'e' in it
# Write a program that reads word.txt
# Prints only the words the have no 'e' in it
# Compute the percentage of words in the list that have no 'e'

TODO:
# CREATE FUNCTION 
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""

def has_no_e(word):
  for letter in word:
    if letter == 'e':
      return False
  return True

def also_has_no_e(word):
  if 'e' in word:
    return False
  else:
    return True

def singleton_has_no_e(word):
    return 'e' in word

# MAIN
fin = open('words.txt')
line = fin.readline()
word_count = 0
no_e_count = 0
for line in fin:
  word = line.strip()
  word_count += 1
  if has_no_e(word):
    print(word)
    no_e_count += 1

print(int(no_e_count/word_count * 100), "% of the words have no 'e'")
