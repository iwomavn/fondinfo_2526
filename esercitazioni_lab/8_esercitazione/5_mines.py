from random import randint

def main():
    w = int(input("Inserisci w: "))
    h = int(input("Inserisci h: "))
    n = int(input("Inserisci n: "))

    matrix = [[0 for _ in range(w)] for _ in range(h)]
    
    for _ in range(n):
        matrix[randint(0, h-1)][randint(0, w-1)] = 1

    with open("output.csv", "w") as file:
        for y in range(h):
            for x in range(w):
                end_ = "\n" if x == w-1 else ","
                print(matrix[y][x], end=end_, file=file)

    coordinate = input("Inserisci coordinate (x,y): ")
    while coordinate != "":
        x, y = coordinate.split(",")
        x = int(x)
        y = int(y)

        if matrix[y][x] == 1:
            print("C'è un 1 nella cella inserita")
        else:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue

                if matrix[ny][nx] == 1:
                    print("C'è un 1 in una cella adiacente")

        coordinate = input("Inserisci coordinate (x,y): ")

if __name__ == "__main__":
    main()

