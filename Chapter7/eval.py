"""
GOAL:
# Create a function eval_loop()
# Iteratively prompts user
# Takes the input and tests using eval
# Print the result
# Continue until user inputs 'done'
# Return the last value evaluated

TO DO:
# CREATE FUNCTION 
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""

def eval_loop():
  last_input = '0'
  while True:
    user_input = input('Input a digit or math expression: ')
    if user_input == 'done':
      break
    print(eval(user_input))
    last_input = user_input
  return eval(last_input)
