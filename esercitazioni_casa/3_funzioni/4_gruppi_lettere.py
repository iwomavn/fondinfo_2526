def count_groups(text: str):
    AM_group, NZ_group = 0, 0
    for i in text:
        if 65 >= ord(i.upper()) <= 77:
            AM_group += 1
        elif 78 >= ord(i.upper()) <= 90:
            NZ_group += 1
    return(AM_group, NZ_group)

def main():
    txt_utent= input("Testo? ")
    # gr_AM, gr_NZ = 0, 0
    gr_AM, gr_NZ = count_groups(txt_utent)
    print(f"Le lettere A-M sono {gr_AM} e le lettere N-Z sono {gr_NZ}")


if __name__ == "__main__":
    main()