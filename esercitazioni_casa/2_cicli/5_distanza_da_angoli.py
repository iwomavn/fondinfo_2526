def main ():
    w = int(input("Inserisci n colonne: "))
    h = int(input("Inserisci n righe: "))
    
    for i in range(h):
        for j in range (w):
            print(i + j, end= " ")
        print()
    print("\n")

    for i in range(h):
        for j in range (w):
            print(j + (h - 1 - i), end= " ")
        print()
    
if __name__ == "__main__":
    main()