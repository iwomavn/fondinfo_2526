def main():
    in_serie, in_parallelo = 0, 0
    with open("resistenze.txt", "r") as f:
        for line in f:
            in_serie += float(line)
            in_parallelo += 1/float(line)
    
    in_parallelo = 1/in_parallelo
    print(in_serie)
    print(in_parallelo)
    
if __name__ == "__main__":
    main()