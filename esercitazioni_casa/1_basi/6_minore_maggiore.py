from random import randint
a = randint(1, 6)
b = randint(1, 6)
c = randint(1, 6)
print(f"I numeri generati: {a}, {b}, {c}")
    
if (a < b) and (a < c):
    print (f"Il minore tra i 3 inseriti è: {a}")
elif (b < c):
    print (f"Il minore tra i 3 inseriti è: {b}")
else:
    print (f"Il minore tra i 3 inseriti è: {c}")