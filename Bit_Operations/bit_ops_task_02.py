#Write python program using user defined functions that will allow you to convert the following into Bits and decimals
a = 0b110111

b = 0b010111100

c = 0b1001000110

#function to change binary to decimal
def bit_to_deci(x):
    return int(x,2)

#for the function to work we need to input the bits as a string.
print(str(a))
print(str(b))
print(str(c))