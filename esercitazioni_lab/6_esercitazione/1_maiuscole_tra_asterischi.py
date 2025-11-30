def shout(s):
    inside = False
    result = ""  # nuova stringa modificata
    for c in s:
        if c == "*":
            inside = not inside
        else:
            if inside:
                c = c.upper()
            result += c  # aggiungiamo il carattere alla nuova stringa
    return result

def main():
    print(shout("amo *me* stessa"))

if __name__ == "__main__":
    main()
