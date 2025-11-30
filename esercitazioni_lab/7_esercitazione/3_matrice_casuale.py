from random import randint

def main():
    w = int(input("Inserisci il numero di righe della matrice: "))
    h = int(input("Inserisci il numero di colonne della matrice: "))
    
    matrix = [chr(randint(97, 122)) for _ in range(w * h)] # comprehension per riempire la matrice
    
    for y in range(w):
        for x in range(h):
            end_ = "\n" if x == h -1 else ","
            print(matrix[x + y * h], end=end_)
            
    c = input("Scegli un carattere: ")
    counter_all = 0
    counter_borders = 0
    
    for y in range(w):
        for x in range(h):
            if matrix[x + y * h] == c:
                counter_all += 1
                if x == 0 or x == h-1 or y == 0 or y == w-1:
                    counter_borders += 1
                
    print(counter_all, counter_borders)
    

if __name__ == "__main__":
    main()
