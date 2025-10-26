from math import pi

def ellipse_area(a, b):
    return pi * a * b

def main():
    a1 = int(input("Primo valore? "))
    b1 = int(input("Secondo valore? "))
    result = ellipse_area(a1, b1)
    print(f"L'area è {result:.02f}")
    
if __name__ == "__main__":
    main()
    