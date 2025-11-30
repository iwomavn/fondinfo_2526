from math import inf

def main():
    file = input("Inserisci nome file: ")
    valori = []
    massimo = -inf
    minimo = inf
    try: 
        with open(file, "r") as f:
            for line in f:
                valori.append(float(line))
    except FileNotFoundError:
        print("File non esiste")
    
    for v in valori:
        if v > massimo:
            massimo = v
            
        if v < minimo:
            minimo = v
            
    print(massimo, minimo)
    
if __name__ == "__main__":
    main()