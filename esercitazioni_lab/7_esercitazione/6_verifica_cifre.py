def digits(n):
    if n <= 0:
        return []
    cifre = [n % 10]
    return cifre + digits(n // 10)


def main():
    n = int(input("n? "))
    lista = digits(n)
    test = 0
    
    for i, l in enumerate(lista):
        test += l * (10**i)

    if test == n:
        print("Giusto!")
    else:
        print("Sbagliato!")

if __name__ == "__main__":
    main()