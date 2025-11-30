def main():
    data = []
    rows, columns = 0, 0
    with open("diagonale.txt", "r") as file_in:
        for line in file_in:
            row = [int(v) for v in line.split(",")]

            columns = len(row)
            rows += 1
            
            for v in row:
                data.append(v)
             
    for y in range(rows):
        for x in range(columns):
            if columns-x == rows-y:
                data[x + y * columns] = data[x + y * columns] ** 2
            
    with open("output_diagonale.txt", "w") as file_out:
        for y in range(rows):
            for x in range(columns):
                end_ = "\n" if x == columns - 1 else ","
                print(data[x + y * columns], end=end_, file=file_out)
   
if __name__ == "__main__":
    main()
