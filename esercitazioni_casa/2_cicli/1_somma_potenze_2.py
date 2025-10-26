n = int(input("Inserisci un numero: "))
somma = 0

for i in range(n):
    somma += 2 ** i
    
print(f"La somma delle prime {n} potenze di 2 è {somma}")
