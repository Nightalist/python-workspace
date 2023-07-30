test = int(2.5)
print(test)

for i in range(1,13): # make sure to use range: iterable value
    print("The number {0:2} squared is {1:3} and cubed is {2:4}"
          .format(i, i**2, i**3))
    
# you can control the line width of string replacement fields 
# by using a colon after the index number for the number of 
# spaces you want the string to occupy


for i in range(1,13): # make sure to use range: iterable value
    print("The number {0:2} squared is {1:<3} and cubed is {2:^4}"
          .format(i, i**2, i**3))
    
    # if you want to left align the values, put a < sign before
    # if you want to center, use a caret ^
    
print()


print("Pi is approximately {0:12} digits long".format(312689/99532))
# default (produces 15 decimals)
print("Pi is approximately {0:12f} digits long".format(312689/99532))
# specifies a floating point value (defaults to 6 values)
print("Pi is approximately {0:12.50f} digits long".format(312689/99532))
# still floating point; but the .50 means 50 points of precision after the point
print("Pi is approximately {0:52.50f} digits long".format(312689/99532))

print("Pi is approximately {0:62.50f} digits long".format(312689/99532))
print("Pi is approximately {0:<72.50f} digits long".format(312689/99532))
print("Pi is approximately {0:<72.54f} digits long".format(312689/99532))


# {0:62.50f}
#  ^ ^  ^ ^
# 1^ the string replacement field index number
# 2^ the line width (spaces, 62 spaces)
# 3^ .50, meaning 50 digits of precision after the dec point
# 4^ f, meaning a floating point value (decimals, default of 6)

# python prioritizes precision over field width, which is why you can 
# have 50 digits in a line width of 12 (line 27)

# IMPORTANT
# The maximum precision of a 
# Python floating point number is between 51 and 53 digits
# it's (apparently) all you'll need

# Lastly, if you leave a field number blank (shown below) it will go in order
# of the replacement fields typed, and the order of the values in .format

for i in range(1,13): # make sure to use range: iterable value
    print("The number {:2} squared is {:<3} and cubed is {:^4}"
          .format(i, i**2, i**3))
  
age = 14  

name = "bob"
    
print("My age is {:2} years old.".format(age))

# as opposed to


print(name + f" is {age} years old.")

pi = 312689/99532

print(f"Pi is approximately {pi:.51f}")

print("bob\tbob")

print(45//5)