def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
    
def mcd_2(a, b):
    mcd = 1
    for i in range(1, a+1):
        if b % i == 0 and a % i == 0:
            mcd = i
    return mcd

def main():
    num1 = int(input("numero 1? "))
    num2 = int(input("numero 2? "))
    print(mcd(num1, num2))
    print(mcd_2(num1, num2))

if __name__ == "__main__":
    main()