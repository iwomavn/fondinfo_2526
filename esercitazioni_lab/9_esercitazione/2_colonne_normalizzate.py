from math import inf

def main():
    matrix = []
    with open("matrice.csv", "r") as file:
        for line in file:
            row = list(map(int, line.strip().split(",")))
            matrix.append(row)
    
    h = len(matrix)
    w = len(matrix[0])

    min_col = []
    max_col = []
    
    for y in range(w):
        minimo = inf
        massimo = -inf
        
        for x in range(h):
            val = matrix[x][y]
            if val < minimo:
                minimo = val
            if val > massimo:
                massimo = val
        
        min_col.append(minimo)
        max_col.append(massimo)

    with open("matrice_normalizzata.csv", "w") as f:
        for x in range(h):
            for y in range(w):
                norm_val = (matrix[x][y] - min_col[y]) / max(1, max_col[y] - min_col[y])
                end_ = "\n" if y == w-1 else ","
                print(norm_val, end=end_, file=f)

if __name__ == "__main__":
    main()
