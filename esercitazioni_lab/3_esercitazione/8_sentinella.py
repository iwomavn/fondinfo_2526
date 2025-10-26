def main():
    while True:
        text = input("Inserisci una stringa (INVIO per terminare): ")
        
        if text == "":
            print("Programma terminato")
            break 

        minuscole_dipari = 0
        minuscole_pari = 0

        for i in range(len(text)):
            if text[i].islower():
                if i % 2 == 0:
                    minuscole_pari += 1
                else:
                    minuscole_dipari += 1

        print(f"Numero di lettere minuscole in posizioni pari: {minuscole_pari}")
        print(f"Numero di lettere minuscole in posizioni dispari: {minuscole_dipari}")

if __name__ == "__main__":
    main()
