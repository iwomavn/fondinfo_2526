from random import randrange

def main():
    n = int(input("Inserisci un n: "))
    lista = [0] * 13
    for i in range(n):
        r1 = randrange(1, 6)
        r2 = randrange(1, 6)
        result = r1 + r2
        lista[result] += 1
        
    for i in lista:
        print(i)
        
if __name__ == "__main__":
    main()