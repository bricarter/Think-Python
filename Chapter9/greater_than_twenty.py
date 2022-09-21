"""
GOAL:
# Write a program that reads word.txt
# Prints only the words with > 20 chars

TODO:
# MAIN
# CREATE VARIABLES
# PRINT EACH VARIABLE ON THEIR OWN LINE
# TEST FORMULA
"""

fin = open('words.txt')
line = fin.readline()
for line in fin:
  word = line.strip()
  if len(word) > 20:
    print(word)
