age = 24
age2  = 14
print("My age is {0} years".format(age, age2))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "July", "Aug", "Oct", "Dec"))

print("There are {0} days in Jan, Mar, May, July, Aug, Oct and Dec"
      .format(31)) # ideal way

print("There are 31 days in Jan, Mar, May, July, Aug, Oct and Dec") # HMM

print("""Jan: {0}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, June: {1}, 
      Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"""
      .format(28, 30, 31))

# you can repeat values (like putting 0 in each curly brace)
# my definition before formal learning
# creates a list of your number variables (or whatever you put in format)
# and you can access them using
# {}, with the number corresponding to the .format value
# the {} are called replacement fields
# these are replcated with the values in the parentheses after .format
# the first value goes into {0}, and so on
# you probably don't want to use string literals inside format