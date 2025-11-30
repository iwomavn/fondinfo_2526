from random import randint

def main():
    w = int(input("w? "))
    h = int(input("h? "))
    matrix = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            matrix[i][j] = randint(0, 9)
    print(f"matrice: ", matrix)

    colums = []
    for j in range(w):
        col = []
        for i in range(h):
            col.append(int(matrix[i][j]))
        colums.append(col)

    nums = colums[0]
    for col in colums[1::]:
        print(col)
        for i, n in enumerate(nums):
            if not n in col:
                del nums[i]
    print("numeri in tutte le colonne", nums)

if __name__ == "__main__":
    main()

