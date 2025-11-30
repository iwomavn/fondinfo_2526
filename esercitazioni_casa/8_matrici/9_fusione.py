def main():
    lista1, lista2 = [], []
    new_lista = []

    with open("file1.txt", "r") as f1:
        for line in f1:
            lista1.append(int(line.strip()))
            
    with open("file2.txt", "r") as f2:
        for line in f2:
            lista2.append(int(line.strip()))

    while lista1 and lista2:
        if lista1[0] <= lista2[0]:
            new_lista.append(lista1.pop(0))
        else:
            new_lista.append(lista2.pop(0))

    new_lista.extend(lista1)
    new_lista.extend(lista2)
    
    with open("output.txt", "w") as f:
        for v in new_lista:
            print(v, file= f)

if __name__ == "__main__":
    main()
