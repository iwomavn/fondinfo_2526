from random import randint 

def main():
    n = int(input("Inserisci un numero positivo (0 per terminare): "))
    counters = [0] * 13
    for _ in range(n):
        risultato = randint(2, 12)
        counters[risultato] += 1
        
    for i, v in enumerate(counters):
        print(f"Risultato {i}: {v} volte")
        

if __name__ == "__main__":
    main()  