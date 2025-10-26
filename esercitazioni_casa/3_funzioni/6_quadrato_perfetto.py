from math import sqrt 

def perfect_square(n):
    i = 0
    while i*i <= n:
        if i*i == n:
            return True, i
        i += 1
    return False, None
        
def main():
   n = int(input("Inserisci n: ")) 
   is_perfect, root = perfect_square(n)
   if is_perfect:
       print(f"è un quadrato perfetto con radice: {root}")
   else:
       print("Non è quadrato perfetto")
       

if __name__ == "__main__":
    main()