def digits(n):
    if n <= 0:
        return []
    
    cifre = [n % 10]
    return cifre + digits(n // 10)

def main():
    print(digits(6543)) 

if __name__ == "__main__":
    main()
