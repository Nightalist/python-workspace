#                   1
#         012345678901234  
parrot = "Norwegian Blue"
#                   0123456  (6 not included)
#print(parrot[0:6]) #Norweg

# telling python to start at position 0 and slice up to but no including position 6
# the last character is NOT included in the slice, this happens in ranges as well

# UP TO BUT NOT INCLUDING. UP TO BUT NOT INCLUDING. UP TO BUT NOT INCLUDING

# print(parrot[-4:-2])  Bl
# print(parrot[-4:12])  also BL, since the index -2 and 12 are the same index

# print(parrot[0:-8])

#print(parrot[0:6:2]) # Nre
#print(parrot[0:6:2]) # Nw

print(parrot[10:6:2])

number = "9,223;372:036 854,775;807"
seperators = (number[1::4])

#print(seperators)

#values = "".join(char if char not in seperators else " " for char in number).split()
#print([int(val) for val in values])

# remember, there is no stop value, so it will go until the end of the string.
# he then adds another colon for his step value of 4. 
# the start value is one, so it will start at the first comma, then print every 
# 4th character (every comma)