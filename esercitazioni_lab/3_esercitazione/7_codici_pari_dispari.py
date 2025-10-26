def main():
    text = input("Inserisci una stringa: ")
    minuscole_dipari = 0
    minuscole_pari = 0
    
    if text != "":
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