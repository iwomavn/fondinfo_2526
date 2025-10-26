def all_alpha (text: str) -> bool:
    for c in text:
        if c < 'A' or c > 'z':
            return False
    return True
    
def main():
    text = input("Inserisci una stringa: ")
    if all_alpha(text):
        print("La stringa contiene solo caratteri alfabetici.")
    else:
        print("La stringa contiene caratteri non alfabetici.")
    
if __name__ == "__main__":
    main()