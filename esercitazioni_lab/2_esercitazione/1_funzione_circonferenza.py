import math

def circumference (radius: float): 
    if radius < 0:
        raise ValueError("Il raggio non può essere negativo")
    else:
        return 2 * math.pi * radius
    
def main():
    radius = float(input("Inserisci il raggio del cerchio: "))
    result = circumference(radius)
    print(f"La circonferenza del cerchio con raggio {radius} è: {result:.2f}")
    
if __name__ == "__main__":
    main()