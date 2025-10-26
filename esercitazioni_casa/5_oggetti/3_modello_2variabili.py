class LinearModel:
    def __init__(self, slope, intercept, c):
        self._a = slope
        self._b = intercept
        self._c = c
        
    def predict(self, x, y):
        return self._a * x + self._b * y + self._c
    

def main():
    x = int(input("x? "))
    y = int(input("y? "))
    model = LinearModel(1, 2, 3)
    print(f"La z è {model.predict(x, y)}")
    
if __name__ == "__main__":
    main()