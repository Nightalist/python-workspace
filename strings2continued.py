#                    1
#         012345678901234  
parrot = "Norwegian Blue"
#                   0123456  (6 not included)
print(parrot[0:6]) #Norweg

# telling python to start at position 0 and slice up to but no including position 6
# the last character is NOT included in the slice, this happens in ranges as well

# UP TO BUT NOT INCLUDING. UP TO BUT NOT INCLUDING. UP TO BUT NOT INCLUDING

print(parrot[3:5])
print(parrot[3:4], parrot[4:5])

print(parrot[0:9])

print(parrot[0:])

print(parrot[:])

# try printing blue

print(parrot[10:])


aleph = "abcdefghijklmnopqrstuvwxyz"


# if you leave the left part of the colon empty,
# it will go to the first character of the string.
# if you leave the right part of the colon empty, 
# it will go to the end of the string.