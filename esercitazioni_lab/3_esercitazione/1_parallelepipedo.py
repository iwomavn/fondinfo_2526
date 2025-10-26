class Parallelepipedo:
    def __init__(self, l: float, h: float, w: float):
        self._l = l
        self._h = h
        self._w = w

    def superficie(self) -> float:
        return (2*(self._l * self._h)+ 2 * (self._l * self._w) + 2 * (self._h * self._w))

    def volume(self) -> float:
       return self._l * self._h * self._w

def main():
    larghezza = float(input("Inserisci la larghezza del parallelepipedo: "))
    altezza = float(input("Inserisci l'altezza del parallelepipedo: "))
    profondita = float(input("Inserisci la profondità del parallelepipedo: "))

    parallelepipedo = Parallelepipedo(larghezza, altezza, profondita)

    print(f"Superficie del parallelepipedo: {parallelepipedo.superficie():.2f}")
    print(f"Volume del parallelepipedo: {parallelepipedo.volume():.2f}")

if __name__ == "__main__":
    main()