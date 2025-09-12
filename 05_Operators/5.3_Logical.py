# Logical Operators :

# Logical operators are used to combine multiple conditions and return a boolean value (True or False).

# Python has 3 logical operators:

# 1. and Operator

# Returns True only if both conditions are True.

# If even one condition is False → result is False.

#  Example:

# x = 10
# print(x > 5 and x < 20)   
# print(x > 15 and x < 20)  

# # 2. or Operator

# # Returns True if at least one condition is True.

# # If both are False → result is False.

# #  Example:

# x = 10
# print(x > 5 or x < 5)    
# print(x < 5 or x > 15)   

# # 3. not Operator

# # Returns the opposite of the condition.

# # If condition is True → not makes it False.

# # If condition is False → not makes it True.

# #  Example:

# x = 10
# print(not(x > 5))    
# print(not(x < 5))    



# Example:

a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))


print("a>b and a>10:", a>b and a>10)
print("a>b or a>10:",a>b or a>10)
print("not (a>b):",not(a>b))