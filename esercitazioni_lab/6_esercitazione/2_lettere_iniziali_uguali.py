def len_common_prefix(a, b):
    lenght = min(len(a), len(b))
    for i in range(lenght):
        if a[i] != b[i]:
            return i
    return lenght

def main():
    txt1 = input("1st text? ")
    txt2 = input("2nd text? ")
    print(len_common_prefix(txt1, txt2))
    
if __name__ == "__main__":
    main()