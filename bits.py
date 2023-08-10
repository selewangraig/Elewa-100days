# Bit Operations
# 3 methods of Bit Operations
# In each method, we will use two concepts
# we will use user-defined functions
# we will use inbuilt funcitons

# Method 1: using inbuilt functions
# bin() - to convert decimal to binary
# int() - to convert binary to decimal

#decimal to binary
def DecimalToBinary(num):
    return bin(num).replace("0b", "")

print(DecimalToBinary(10))

#binary to decimal
def BinaryToDecimal(num):
    return int(num,2)

print(BinaryToDecimal("1010"))