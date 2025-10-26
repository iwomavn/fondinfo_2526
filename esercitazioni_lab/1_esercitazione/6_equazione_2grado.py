a=int(input("Inserisci il coefficiente a: "))
b=int(input("Inserisci il coefficiente b: "))
c=int(input("Inserisci il coefficiente c: "))

if (a==0):
    print("Non è un'equazione di secondo grado")
elif (b**2-4*a*c)<0:
    print("L'equazione non ha soluzioni reali")
elif (b**2-4*a*c)==0:
    print("L'equazione ha una soluzione reale")
else:
    print("L'equazione ha due soluzioni reali distinte")