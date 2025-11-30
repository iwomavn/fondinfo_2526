def spiral(rows, cols):
    matrix = [[0] * cols for _ in range(rows)]
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # destra, giù, sinistra, su
    
    d_index = 3 # iniziamo andando su
    y, x = rows - 1, 0  # posizione iniziale

    for num in range(1, rows * cols + 1):
        matrix[y][x] = num
        dy, dx = directions[d_index]
        next_y, next_x = y + dy, x + dx

        if not (0 <= next_y < rows and 0 <= next_x < cols and matrix[next_y][next_x] == 0): # se è fuori matrice vertic., orizz., o è già piena
            d_index = (d_index + 1) % 4 # nuovo indice
            dy, dx = directions[d_index] 
            next_y, next_x = y + dy, x + dx

        y, x = next_y, next_x

    return matrix

def main():
    rows = int(input("Inserisci righe matrice: "))
    cols = int(input("Inserisci colonne matrice: "))
    matrice = spiral(rows, cols)
    
    for y in range(rows):
        for x in range(cols):
            end_ = "\n" if x == cols -1 else " "
            print(matrice[y][x], end = end_)
    
if __name__ == "__main__":
    main()