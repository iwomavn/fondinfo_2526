def fill (lista, i):
    if lista[i] != 0:
        return
    elif lista[i] == 0:
        lista[i] = 1
        
        if lista[i-1] == 0:
            fill(lista, i-1)
            
        if lista[i+1] == 0:
            fill(lista, i+1)
            
    return lista
            
def main():
    lista = [0,0,2,2,0,0,0,0,0,0,0,2,0,0,0]
    result = fill(lista, 9)
    print(result)
    
if __name__ == "__main__":
    main()