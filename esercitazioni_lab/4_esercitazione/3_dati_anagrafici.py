class Person:
    def __init__(self, name, surname, year, month, day):
        self._name = name
        self._surname = surname
        self._year = year
        self._month = month
        self._day = day
        
    def age(self, year, month, day):
        anni = year - self._year
        if (self._month == month) and (self._day > day) or (self._month > month):
            anni -= 1
            return anni
        else: 
            return anni
    
    def describe(self) -> str:
        anni = self.age(2025, 10, 26)
        return f"{self._name} {self._surname}, age: {anni} years, born on {self._year}/{self._month}/{self._day}"
    
    def name(self):
        return self._name
    
def main():
    person = []
    for i in range(3):
        name = input("Inserisci nome: ")
        surname = input("Inserisci cognome: ")
        year = int(input("Inserisci anno nascita: "))
        month = int(input("Inserisci mese nascita: "))
        day = int(input("Inserisci anno nascita: "))
    
        person.append(Person(name, surname, year, month, day))
        print(person[i].describe())

    for p in person:
        anno = int(input("Inserisci anno: "))
        mese = int(input("Inserisci mese: "))
        giorno= int(input("Inserisci giorno: "))
        
        if p.age(anno, mese, giorno) >= 18:
            print(f"{p.name()} è maggiorenne")
    
        
if __name__ == "__main__":
    main()
   