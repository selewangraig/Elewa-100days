#define the statements
p = True
q = False
r = True

#question 1; (p ∨ ¬q) and q
a = p or (not q) #(p ∨ ¬q) #True
b = a and q #False

print(f"Answer to question 1: {b}")

#question 2; (p or q) not (¬q and ¬p)
c = p or q #(p or q) #True
d = not(q and p) #(¬q and ¬p) #True
e = not d #not (¬q and ¬p) #False
f = c and e #False

print(f"Answer to question 2: {f}")

#question 3; (p ∨ q) ∧ (p or  ¬ q)
g = p or q #(p ∨ q) #True
h = p or (not q) #(p or  ¬ q) #True
i = g and h #True

print(f"Answer to question 3: {i}")

#question 4; p ∨ (q ∧ r)
j = q and r #(q ∧ r) #True
k = p or j #True

print(f"Answer to question 4: {k}")

#question 5; ¬(p ∧ q) ∨ (p ∨ q)
l = not(p and q) #¬(p ∧ q) #True
m = p or q #(p ∨ q) #True
n = l or m #True

print(f"Answer to question 5: {n}")