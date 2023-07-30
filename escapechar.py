splitString = "This string has been \n split over \n several \n lines"
print(splitString)

tabbedString = "1 \t 2 \t 3 \t 4 \t 5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,... he\'s resting".' )
# or 
print("The pet shop owner said \"No, no, 'e's uh,... he's resting\".")
#if you want to use the same quote you make a string with, you need with escape it with a backslash

print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# triple quotes eliminate the need to escape any quotes, and can also be used for multi-line

anotherSplitStringfalse = """This string has been \
split over \
several \
lines"""

print(anotherSplitStringfalse)

anotherSplitStringtrue = """This string has been 
split over 
several 
lines\n"""

print(anotherSplitStringtrue)

# \can also be used to escape the end of a line

print("""The pet shop owner said "No, no, \
'e's uh,... he's resting".""")

print("\n")

print("C:\\Users\\siawto\\documents\\homeworkfolder.txt")

# there are two ways to include a backslash in the raw string literal. 
# you can just put... another backslash!

print(r"C:\Users\siawto\documents\homeworkfolder.txt")

# you can also use an 'r' before the quotations of your string, 
# which makes the string raw (not recommended)
