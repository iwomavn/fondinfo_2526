class Quadratic:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    def predict(self, x):
        return self._a * x **2 + self._b * x + self._c
    
def main():
    x = int(input("x? "))
    model = Quadratic(1, 2, 3)
    print(f"La y è {model.predict(x)}")
    
if __name__ == "__main__":
    main()