def cels_to_fahr(cels_temp: float) -> float:
    return cels_temp * 1.8 + 32

def main():
    temp = float(input("Inserire temperatura: "))
    result = cels_to_fahr(temp)
    print(f"La temperatura in fahrenheit: {result:.02f}")
    
if __name__ == "__main__":
    main()