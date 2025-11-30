def clamp(lista, a, b):
    for i in range(len(lista)):
        if lista[i] < a:
            lista[i] = a
        elif lista[i] > b:
            lista[i] = b
            
def main():
    data = [3, 4, 6, 7, 3, 5, 6, 12, 4]
    clamp(data, 5, 10)
    
    for v in data:
        print(v, end= " ")
        
if __name__ == "__main__":
    main()