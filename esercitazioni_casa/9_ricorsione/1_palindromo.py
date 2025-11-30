def is_palindromo(text):
    last = len(text)
    
    if last <= 1: # caso base
        return True
    elif text[0] == text[last-1]: # se primo e ultimo elemento sono uguali
        return is_palindromo(text[1:last-1]) # rifaccio senza primo e ultimo elemento
    else:
        return False
    
def main():
    print(is_palindromo("ciao"))
    print(is_palindromo("assa"))
    
main()