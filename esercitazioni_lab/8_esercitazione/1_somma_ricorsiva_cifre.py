def digits(n):
    if n == 0:
        return []
    d = n % 10 # ultima cifra
    return [d] + digits(n // 10) # + resto numero rifaccio stessa cosa

def sum_digits(n):
    if n < 10:
        return n
    cifre_n = digits(n)
    total = sum(cifre_n)
    return sum_digits(total) # se è minore di 10 returna il numero stesso in if sennò risomma
    
def main():
    print(sum_digits(41))
    print(sum_digits(327))
    
if __name__ == "__main__":
    main()
