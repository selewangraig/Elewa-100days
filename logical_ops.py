# Logical Operations in Python

a = 10
b = 4

# and - both conditions must be true
print(f"Is {a} greater than 5 and {b} less than 10? {a > 5 and b < 10}")

# or - either condition must be true
print(f"Is {a} greater than 5 or {b} greater than 10? {a > 5 or b > 10}")

# not - reverses the condition
print(f"Is {a} greater than 5? {not a > 5}")


#Demonstration of using logical operations
p = True
q = False
r = True

#task_1
a = p or q #True
aa = a and r #True
b = p and r #True
c = q and r #False

ans_1 = aa or b or c #True
#print(ans_1)

#task_2
d = not(p and q) #True
e = q and (not r) #False

ans_2 = d or e #True
#print(ans_2)