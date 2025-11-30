def main():
    rows, cols = 4, 24
    matrix = list(map(chr, range(31, 128)))
    
    print("\nMatrice (colonna per colonna):")
    for y in range(rows):
        for x in range(cols):
            end_ = "\n" if x == cols - 1 else " "
            print(matrix[x * rows + y], end=end_)
    
    print("Matrice (riga per riga):")
    for y in range(rows):
        for x in range(cols):
            end_ = "\n" if x == cols - 1 else " "
            print(matrix[x + y * cols], end=end_)
    
main()