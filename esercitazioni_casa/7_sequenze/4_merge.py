def merge (lista1, lista2, lista):
    i1, i2 = 0, 0
   
    while len(lista1) > 0 and len(lista2) > 0:
        if lista1[i1] <= lista2[i2]:
            lista.append(lista1.pop(i1))
        else:
            lista.append(lista2.pop(i2))

def main():
    lista1 = [1, 3,23,4]
    lista2 = [2,89,6,1 ]
    lista1.sort()
    lista2.sort()
    lista = []
    merge(lista1, lista2, lista)
    print (lista)
    
if __name__ == "__main__":
    main()