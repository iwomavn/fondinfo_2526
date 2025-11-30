from random import randrange

def shuffle(lista):
    for i in range(len(lista)):
        j = randrange(len(lista))
        temp_j = lista[j]
        lista[j] = lista[i]
        lista[i]= temp_j
        
def main():
    lista = [1, 2, 3, 4, 5]
    shuffle(lista)
    for v in lista:
        print(v, end= " ")

if __name__ == "__main__":
    main()