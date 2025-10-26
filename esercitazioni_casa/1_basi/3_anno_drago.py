anno = int(input("Inserisci il tuo anno di nascita: "))

if (anno - 2024) % 12 == 0:
    print(f"Il {anno} era l'anno del drago!")
else:
    print(f"Il {anno} non era l'anno del drago!")