def find_max(lista):
    if isinstance(lista, str):
        return lista # se è una stringa e non una lista, returna la stringa stessa
    elif isinstance(lista, list):
        max = None # massimo 
        for l in lista: # scorro ogni elemento nella lista
            l_max = find_max(l) # se è una stringa mi returna la stringa
            if max is None or l_max > max:
                max = l_max # Ann
        return max

def main():
    print(find_max(["Ann", ["Bart", ["Carol", "Cindy"], "Bob", "Art"], ["Bea"], "Bill"]))

if __name__ == "__main__":
    main()
