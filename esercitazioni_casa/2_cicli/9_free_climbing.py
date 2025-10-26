from random import randint

TOP = 10
first_climber, second_climber = 0, 0

while first_climber < TOP and second_climber < TOP:
    first_climber += randint (-1, 3)
    second_climber += randint (-1, 3)
    print(f"Primo arrampicatore: {first_climber}")
    print(f"Secondo arrampicatore: {second_climber}")
    
    if first_climber < 0: 
        first_climber = 0
    
    if second_climber < 0:
        second_climber = 0

if first_climber > TOP:
    print("Ha vinto il primo arrampicatore!")    
else:
    print("Ha vinto il secondo arrampicatore!")    