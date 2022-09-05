"""
GOAL:
# Create a function ack(m, n)
# Evaluates the Ackerman function
# Test ack(3,4), should return 125

TODO:
# CREATE FUNCTION 
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""


def ack(m, n):
  if m==0:
    return n+1
  elif m > 0 and n == 0:
    return ack(m-1, 1)
  elif m > 0 and n > 0:
    return ack(m-1,ack(m,n-1))
  else:
    return

# MAIN
print(ack(20,25))
