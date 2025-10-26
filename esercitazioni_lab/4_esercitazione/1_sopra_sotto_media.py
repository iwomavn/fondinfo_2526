def main():
    numbers = []
    print("Inserisci una sequenza di numeri interi (termina con 0):")
    n = int(input())
    while n != 0:
        numbers.append(n)
        n = int(input())
        
    if len(numbers) == 0:
        print("Nessun numero è stato inserito.")
        return
    
    somma = 0
    for i in numbers:
        somma += i
    media = somma / len(numbers)
    print(f"Media {media:.2f}")

    sotto_media, sopra_uguale_media = [], []
    for i in numbers:
        if i < media:
            sotto_media.append(i)
        else:
            sopra_uguale_media.append(i)
    
    print("Numeri sotto la media:")
    for num in sotto_media:
        print(num)              
    
    print("Numeri sopra o uguali alla media:")
    for num in sopra_uguale_media:
        print(num)

if __name__ == "__main__":
    main()
