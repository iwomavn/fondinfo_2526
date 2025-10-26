values = []
val = int(input("Inserisci valore resistenza: "))

while val != 0:
    values.append(val)
    val = int(input("Inserisci valore resistenza: "))

in_serie = 0
in_parallelo = 0
for i in values:
    in_serie += i 
    in_parallelo += 1 / i
    
print(f"Resistenza in serie: {in_serie} ohm")
print(f"Resistenza in parallelo: {in_parallelo:.2f} ohm")