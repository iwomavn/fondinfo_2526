def triangle_perimeter(a, b, c):
    if (a > (c+b)) or (b>(c+a)) or (c>(a+b)):
        raise ValueError("I lati non formano un trinagolo")
    else:
        return a + b + c
    
def main():
    choice = 1
    while choice != 0:    
        a1 = int(input("Lato 1? "))
        b1 = int(input("Lato 2? "))
        c1 = int(input("Lato 3? "))
        result = triangle_perimeter(a1, b1, c1)
        print(f"Il perimetro è {result}")
        choice = int(input("Vuoi elaborare altri dati? (SI = 1\t NO = 0) "))
        
if __name__ == "__main__":
    main()