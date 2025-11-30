def polish_notation(tokens):
    t = tokens.pop(0) # primo valore della seguenza
    
    if t.isdigit():
        return int(t) # se è numero lo ritorno
    
    # sennò ...
    l = polish_notation(tokens) # rifaccio sta volta togliendo il primo
    r = polish_notation(tokens) # rifaccio senza i primi due elementi 
    
    # vediamo che operatore è
    if t == "+":
        return l + r
    elif t == "-":
        return l - r
    elif t == "*":
        return l * r
    else:
        return l/r

def main():
    value = "+ 2 7" 
    
    tokens = []
    tokens = value.split() # la divido e metto in una lista
    
    print(polish_notation(tokens))
    
if __name__ == "__main__":
    main()