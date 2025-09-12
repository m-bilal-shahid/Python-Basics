
#  Identity Operators:

#  Identity operators are used to compare the memory location of two objects 
# (whether they are the same object in memory, not just equal in value).

# Python has 2 identity operators:

# 1. is

# Returns True if both variables point to the same object in memory.

#  Example:

# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]

# print(x is y)   # True
# print(x is z)   # False )

# 2. is not

# Returns True if both variables do not point to the same object in memory.

#  Example:

# x = [1, 2, 3]
# y = [1, 2, 3]

# print(x is not y)   


#  Quick Note:

# == checks values.

# is checks identity (memory address).

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)   # True  (same values)
# print(a is b)   # False (different objects in memory)



#with integers identity operator will give true 
# with complexity (lists,dicts,etc) it will give false


# a=100
# b=100
# print(a is b)


# Example:

a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

print("a is b:",a is b)
print("a is not b:",a is not b)


list1=[2,3,5,6]
list2=[2,3,5,6]
print("List 1:",list1)
print("List 2:",list2)


print("List1 is List2:", list1 is list2)
print("List1  is not List2:", list1 is not list2)