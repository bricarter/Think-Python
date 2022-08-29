"""
GOAL:
# Write a script that reads the current time
# Convert the current time into hours, minutes, and seconds
# Convert the current time into the number of days since the epoch
# Use the time module
# The time function in the time module returns the curren GMT
# Epoch is 1 January 1970


TODO:
# SET BASE CASE
# CREATE RECURSION

# CREATE FUNCTION 
# SET PARAMETERS
# SET RETURN TYPE
# SET RETURN VALUE
"""

import time

def SecondsSinceEpoch():
 return time.time()

def MinutesSinceEpoch():
 minutes_since_epoch = SecondsSinceEpoch() // 60
 return minutes_since_epoch

def HoursSinceEpoch():
 hours_since_epoch = MinutesSinceEpoch() // 60
 return hours_since_epoch

def DaysSinceEpoch():
 days_since_epoch = HoursSinceEpoch() // 24
 print(int(days_since_epoch), 'days since epoch')
 return days_since_epoch

def CurrentHour(hours):
 if hours < 24:
  return hours
 else:
  return CurrentHour(hours/24)

def CurrentMinutes(hours):
 current_minutes = (CurrentHour(hours) * 60) % 60
 return current_minutes 

def CurrentSeconds(hours):
 current_seconds = (CurrentMinutes(hours) * 60) % 60
 return current_seconds 

# MAIN
DaysSinceEpoch()
current_hours = CurrentHour(HoursSinceEpoch())
current_minutes = CurrentMinutes(HoursSinceEpoch())
current_seconds = CurrentSeconds(HoursSinceEpoch())
print('Current time: ', int(current_hours), ':', int(current_minutes), ':', int(current_seconds))
