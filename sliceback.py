letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1] # you'll often see this as the reverse of said string
# because we are using a negative step, 
# our start value must be greater than our stop value
# with a negative step, the start value defaults to the end of the string 
# and the stop value defaults to the start of the string
#print(backwards)

print(letters[-10:-13:-1])

print(letters[4::-1])

print(letters[:17:-1])

print(letters[-4:])

# common Python slice idiom

# [::1] - reversing a sequence

# - [-x:] last x items of a sequence. negative start value and defaults for stop and step
# it just returns the end of the sequence
# can also be used to get the last item of a sequence, by using [-1:]
print(letters[-1:]) # z
# you can also get the first items of a sequence 
# by putting a positive number in the stop value [:1] or [0]
print(letters[:1]) # a
# but what if your string is empty? (say the letter variables has nothing)
# [0] would crash with an index error, while [:1] will just return nothing 
# (since the sequence is empty)
