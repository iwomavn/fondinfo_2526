def count_groups(text: str) -> tuple[int, int]:
    a_m = 0
    n_z = 0
    for char in text:
        if 'a' <= char.lower() <= 'm':
            a_m += 1
        elif 'n' <= char.lower() <= 'z':
            n_z += 1
    return (a_m, n_z)

def main():
    while True:
        text = input("Inserisci una riga di testo (vuota per terminare): ")
        if text == "":
            break
        a_m, n_z = count_groups(text)
        print(f"Lettere A-M: {a_m}, Lettere N-Z: {n_z}")

if __name__ == "__main__":
    main()