#Define the statements
a = True
b = False
c = True

p = True
q = False

#Question 1; a and (b ∧ ¬c) = a or (b ∧ (¬c)).
var_1 = b and (not c) #(b ∧ ¬c) #False
var_2 = a and var_1 #a and (b ∧ ¬c) #False

var_3 = b and (not c) #(b ∧ ¬c) #False
var_4 = a or var_3 #a or (b ∧ ¬c) #True

print(f"Answer to question 1: {var_2 == var_4}")

#Question 2; (p ∧ q) ∨ (¬p ∧ q) ∨ (¬p ∧ ¬q).
var_3 = p and q #(p ∧ q) #False
var_4 = (not p) and q #(¬p ∧ q) #False
var_5 = (not p) and (not q) #(¬p ∧ ¬q) #False
var_6 = var_3 or var_4 or var_5 #False

print(f"Answer to question 2: {var_6}")
