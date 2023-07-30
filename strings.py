print('Today is a good day to learn python')
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
# there is no difference between single or double quotes in python. it just means you can use the other in the string
print("hello" + ' world \n')
# you can use '+' to concatcenate strings and such

greeting = 'Hello'
name = input("Please enter your name!" + "\n")

#if input == ("no" | "No") {
#    print("Alright. Have a good day.")
#}


#print("\n"+ greeting + ' ' + name + "\n")


age = 24
print(age)

print(type(age))
print(type(greeting))

age = "2 years"
print(age)
print(type(age))

# the code above proves the fact that python variables can change data type, 
# unlike other languages like C and Java

age = 24
print(age)

print(type(age))
print(type(greeting))

#ageInWords = input("How old are you?\n")
#print(name + " is " + ageInWords + " years old!")
#print(type(age))


print("My age is {:2} years old.".format(age))

# as opposed to

print(name + f" is {age} years old.")

pi = 312689/99532

print(f"Pi is approximately {pi:.51f}")