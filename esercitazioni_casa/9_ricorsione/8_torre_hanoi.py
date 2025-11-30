def hanoi(n, start, dest, aux):
    if n == 1: # solo un disco, caso base
        print(f"Sposto disco 1 da {start} a {dest}")
        return
    
    hanoi(n-1, start, aux, dest)
    print(f"Sposto disco {n} da {start} a {dest}")
    hanoi(n-1, aux, dest, start)

def main():
    n= 3
    hanoi(n, "a", "c", "b")
    
if __name__ == "__main__":
    main()