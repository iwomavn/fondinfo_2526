while (int(input("Vuoi risolvere un'equazione di secondo grado? (1 o 0) "))):
    a=int(input("Inserisci il coefficiente a: "))
    b=int(input("Inserisci il coefficiente b: "))
    c=int(input("Inserisci il coefficiente c: "))

    if (a==0):
        print("Non è un'equazione di secondo grado")
    elif (b**2-4*a*c)<0:
        print("L'equazione non ha soluzioni reali")
    elif (b**2-4*a*c)==0:
        x=-b/(2*a)
        print(f"L'equazione ha una soluzione reale doppia: {x}")
    else:
        x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
        print(f"L'equazione ha due soluzioni reali distinte: {x1} e {x2}")