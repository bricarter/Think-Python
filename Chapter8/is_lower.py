def any_lowercase1(s):
 """Evaluates if the first char of the given string (s) is lowercase, returns the boolean value
 """
 for c in s:
  if c.islower():
   return True
  else:
   return False

def any_lowercase2(s):
 """Evaluates if 'c' is lowercase, returns the boolean value
 """
 for c in s:
  if 'c'.islower():
   return 'True'
  else:
   return 'False'

def any_lowercase3(s):
 """Evaluates if the chars of the given string (s) are lowercase, returns the boolean value of the last char evaluated"""
 for c in s:
  flag = c.islower()
 return flag

def any_lowercase4(s):
 """Evaluates if any of the chars of the given string (s) are lowercase, returns True if any lowercase char is detected"""
 flag = False
 for c in s:
  flag = flag or c.islower()
 return flag

def any_lowercase5(s):
 """Evaluates if any of the chars of the given string (s) are not lowercase, returns False if any uppercase char is detected"""
 for c in s:
  if not c.islower():
   return False
 return True 
