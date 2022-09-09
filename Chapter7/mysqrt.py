mysqrt.py

"""
#GOAL:
# Copy the loop and encapuslate it into a function mysqrt()
# Paramters: a
# Returns an estimate of the square root of a
# Create a function test_square_root
# Creates a table testing mysqrt(a) against math.sqrt(a)

TODO:
# TEST FORMULA
# CREATE FUNCTION 
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""
import math

def mysqrt(a):
  x = a / 2
  while True:
    #print(x)
    y = (x + a / x) /2
    if abs(x - y) < .0000001:
      break
    x = y
  return x

def setup_table():
  print('a\tmysqrt(a)\tmath.sqrt(a)\tdiff')
  for i in range(len('a')):
    print('-', end='')
  print('\t', end='')
  for i in range(len('mysqrt(a)')):
    print('-', end='')
  print('\t', end='')
  for i in range(len('math.sqrt(a)')):
    print('-', end='')
  print('\t', end='')
  for i in range(len('diff')):
    print('-', end='')
  print('\n')

def test_square_root():
  setup_table()
  for i in range(10):
    if i == 0:
      pass
    else:
      print(i,'\t', mysqrt(i), math.sqrt(i), abs(mysqrt(i) - math.sqrt(i)))
