def smooth(matrix: float):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for y in range(rows):
        for x in range(cols):
            value = matrix[y][x]
            valueup = matrix[y - 1][x] if y > 0 else 0
            valuedown = matrix[y + 1][x] if y < rows - 1 else 0
            valuesx = matrix[y][x - 1] if x > 0 else 0
            valuedx = matrix[y][x + 1] if x < cols - 1 else 0
            total = value + valueup + valuedown + valuesx + valuedx
            new_matrix[y][x] = total / 5
    
    return new_matrix

def main():
    matrice = [[1, 2, 3, 4, 5],        
        [5, 6, 7, 8, 9],
        [9, 10, 11, 12, 13]]
    
    new_matrice = smooth(matrice)
    for row in new_matrice:
        print(row)
        
        
if __name__ == "__main__":
    main()