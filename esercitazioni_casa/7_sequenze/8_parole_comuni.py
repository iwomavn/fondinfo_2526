def confronta(str1, str2):
    lista1 = str1.split()
    lista2 = str2.split()
    lista_comuni = []
    
    for v in lista1:
        if v in lista2:
            lista_comuni.append(v)
            
    return lista_comuni

def main():
    lista = confronta("i love you", "you love me")
    for v in lista:
        print(v)
        
if __name__ == "__main__":
    main()