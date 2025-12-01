def main():
    parole = {} # dizionario 
    lista = []

    with open("g2d.py", "r") as file:
        for line in file:
            words = line.split()
            lista.append(words)

    for riga in lista:         # riga = lista di parole
        for p in riga:         # p = singola parola
            if p not in parole:
                parole[p] = 1
            else:
                parole[p] += 1

    for k, v in parole.items():
        print(k, v)
        
    top10 = sorted(parole.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Le 10 parole più frequenti: ")
    for parola, count in top10:
        print(parola, count)
    
if __name__ == "__main__":
    main()
