def recursive_pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    elif n > 0:  # caso ricorsivo per n positivo
        return x * recursive_pow(x, n - 1)

def main():
    x = float(input("Inserisci la base (x): "))
    n = int(input("Inserisci l'esponente (n): "))
    
    risultato = recursive_pow(x, n)
    print(f"{x} elevato alla potenza di {n} è: {risultato}")
    
main()