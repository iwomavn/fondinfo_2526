from math import pi, sqrt

class Ellypse:
    def __init__(self, a, b):
        self._a = a
        self._b = b
        
    def area (self) -> float:
        return pi * self._a * self._b
    
    def fuoco (self) -> float:
        return sqrt(abs(self._a ** 2 - self._b ** 2))
    
def main():
    a = int(input("a? "))
    b = int(input("b? "))
    ellisse = Ellypse(a, b)
    print(f"L'area è {ellisse.area():.02f} e il fuoco è {ellisse.fuoco()}")
    
if __name__ == "__main__":
    main()