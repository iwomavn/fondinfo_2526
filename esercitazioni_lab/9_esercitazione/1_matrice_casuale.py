from random import randint

def main():
    w = int(input("w? "))
    h = int(input("h? "))

    matrix = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(w*h):
        y = randint(0, h-1)
        x = randint(0, w-1)
        
        while matrix[y][x] != 0:
            y = randint(0, h-1)
            x = randint(0, w-1)
        
        matrix[y][x] = i

    with open("matrice.csv", "w") as file:
        for y in range(h):
            for x in range(w):
                end_ = "\n" if x == w-1 else ","
                print(matrix[y][x], end=end_, file=file)
                 
if __name__ == "__main__":
    main()
