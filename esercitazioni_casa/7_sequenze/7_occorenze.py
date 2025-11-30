def occorrenze(text):
    text_list = text.split()
    dizionario = {}
    
    for v in text_list:
        if v in dizionario:
            dizionario[v] += 1
        else:
            dizionario[v] = 1
            
    return dizionario

def main(): 
    print(occorrenze("i love you and you love me"))
 
if __name__ == "__main__":
    main()