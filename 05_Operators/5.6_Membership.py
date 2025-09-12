# Membership Operators:
# Membership operators are used to check if a value exists
#  inside a sequence (like string, list, tuple, set, or dictionary).


# 1. in

#  Returns True if the value exists in the sequence.

# print(5 in [1, 2, 3, 4, 5])   
# print("a" in "apple")         

# 2. not in

#  Returns True if the value does NOT exist in the sequence.

# print(10 not in [1, 2, 3, 4, 5])   
# print("z" not in "apple")          



word=input("Enter A Word:")
char=input("Enter A Character:")

print("Character in Word:",char in word)
print("Character not in Word:",char not in word)