def anagrams(str):
    results = []
    
    if str == "":
        return [""]
    else:
        for i, s in enumerate(str):
            resto = str[:i] + str[i+1:]
            permutazioni = anagrams(resto)
            for p in permutazioni:
                results.append(s + p)
    return results

def main():
    print(anagrams("elvis"))
    
if __name__ == "__main__":
    main()