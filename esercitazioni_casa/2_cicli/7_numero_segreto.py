import random
secret_number = random.randint(1, 90)

guess = int(input("Indovina il numero segreto (tra 1 e 90): "))
while (guess != secret_number):
    if guess < secret_number:
        print("Il numero è minore del numero segreto. Riprova.")
    else:
        print("Il numero è maggiore del numero segreto. Riprova.")
    guess = int(input("Indovina il numero segreto (tra 1 e 90): "))
print("Complimenti! Hai indovinato il numero segreto.")
        