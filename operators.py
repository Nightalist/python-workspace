a = 12
b = 3

print(a + b)    # should be 15, right? 
print(a - b)    # should be 9, right?
print(a * b)    # should be 36, right?

# there is a difference between dividing with '/' and '//'.
# dividing with / will always give you a float value

print(a / b)    # should be 4.0, right?

# dividing with // is integer division, with gives you an int.
# integer division is rounded down towards minus infinity

print(a // b)   # should be 4, right?

print(a % b)    # calculates the remainder after integer division. 
                # (modulo) should be 0, right?
print()

#for i in range(1, a//b): # range only takes integer values
#    print(i)

# a is 12, b is 3
# PEMDAS, operator precendence

print(a + b / 3 - 4 * 12)

# a + 1 - 48

# 12 + 1 - 48
   
# 13 - 48 (-35)

print(a + (b / 3) - (4 * 12))