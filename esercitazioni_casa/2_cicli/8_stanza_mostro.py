from random import randint
monster = (randint(0, 4), randint(0, 4))
tresure = (randint(0, 4), randint(0, 4))
pos = (randint(0, 4), randint(0, 4))

print(f"Il mostro è qui: {monster}")
print(f"Il tesoro è qui: {tresure}")

while monster == tresure:
    tresure = (randint(0, 4), randint(0, 4))

while pos == monster or pos == tresure:
    pos = (randint(0, 4), randint(0, 4))

while pos != tresure and pos != monster:
    print(f"La tua posizione è {pos}")
    
    direzione = input("Dove vuoi muoverti? (WASD)?")
    x, y = pos
    
    if direzione == "W" or direzione =="w":
        y -= 1
    elif direzione == "A" or direzione == "a":
        x -= 1
    elif direzione == "S" or direzione =="s":
        y += 1
    elif direzione == "D" or direzione =="d":
        x += 1
    
    pos = (x, y)
    
    if pos == tresure:
        print("Hai vinto")
    elif pos == monster:
        print("Hai perso")

        
    
                
        
        