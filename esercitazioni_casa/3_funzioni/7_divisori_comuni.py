def common_divisors(a, b):
    divisors = []
    for i in range(1, (a+1)):
        if ((a % i) == 0) and ((b % i)) == 0:
            divisors.append(i)
    return divisors

def main():
    n1 = int(input("Inserisci primo numero: "))
    n2 = int(input("Inseeisci il secondo numero: "))
    result = []
    result = common_divisors(n1, n2)
    print("I divisori comuni sono: ")
    for i in result:
        print(i, end=" ")
        
if __name__ == "__main__":
    main()