from random import randint
def randchar(sup_lim, inf_lim):
    return chr(randint(inf_lim, sup_lim))

def main():
    print("Carattere casuale maiuscolo:", randchar(90, 65))  
    print("Carattere casuale minuscolo:", randchar(122, 97))
    
if __name__ == "__main__":
    main()