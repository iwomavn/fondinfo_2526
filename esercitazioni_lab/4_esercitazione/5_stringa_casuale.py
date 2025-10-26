import random
def add_letter (string: str):
    return string + chr(random.randint(97, 123))

def main():
    n = int(input("Lunghezza della stringa casuale: "))
    stringa = ""
    for _ in range(n):
        stringa = add_letter(stringa)
    print(stringa)
    
if __name__ == "__main__":
    main()