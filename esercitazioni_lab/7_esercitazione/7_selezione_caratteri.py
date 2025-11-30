def select_chars(txt):
    result = ""
    for i in range(len(txt)):
        c = txt[i]
        if i > 0 and i < len(txt)+1:
            if not (ord(txt[i]) <= ord(txt[i-1]) or ord(txt[i]) <= ord(txt[i+1])):
                result += c
    return result

def main():
    selected = select_chars("testo di prova")
    print("Caratteri selezionati:", selected)

if __name__ == "__main__":
    main()
