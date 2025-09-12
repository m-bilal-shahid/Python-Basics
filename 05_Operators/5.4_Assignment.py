# # Assignment Operators :
# # Assignment operators are used to assign values to variables
# # and also combine assignment with an operation.

# # 1. = (Simple Assignment)
# #  → assigns value to variable
# x = 10
# print("1. = (Simple Assignment):", x)   

# # 2. += (Add and Assign) 
# # → adds right operand and assigns result
# x = 5
# x += 3   # same as x = x + 3
# print("2. += (Add and Assign):", x)  

# # 3. -= (Subtract and Assign) 
# # → subtracts right operand and assigns result
# x = 10
# x -= 4   # same as x = x - 4
# print("3. -= (Subtract and Assign):", x)  

# # 4. *= (Multiply and Assign) 
# # → multiplies right operand and assigns result
# x = 4
# x *= 3   # same as x = x * 3
# print("4. *= (Multiply and Assign):", x)  

# # 5. /= (Divide and Assign) → divides and assigns result
# x = 10
# x /= 2   # same as x = x / 2
# print("5. /= (Divide and Assign):", x)  

# # 6. //= (Floor Divide and Assign) → floor division and assigns result
# x = 10
# x //= 3   # same as x = x // 3
# print("6. //= (Floor Divide and Assign):", x) 

# # 7. %= (Modulus and Assign) → modulus and assigns result
# x = 10
# x %= 3   # same as x = x % 3
# print("7. %= (Modulus and Assign):", x)  

# # 8. **= (Exponent and Assign) → raises to power and assigns result
# x = 2
# x **= 3   # same as x = x ** 3
# print("8. **= (Exponent and Assign):", x)  


# Example:


a=int(input("Enter A Number:"))
print("After =", a)
a+=5
print("After +=5", a)
a-=2
print("After -=2", a)
a*=2
print("After *=2 ", a)
a/=2
print("After /=2", a)
a//=2
print("After //=2", a)
a%=2
print("After %=2", a)
a**=2
print("After **=2", a)