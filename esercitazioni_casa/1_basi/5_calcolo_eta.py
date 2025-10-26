nascita = [int(input("Inserisci il tuo anno nascita: ")), int(input("Mese nascita: ")), int(input("Giorno nascita: "))]
oggi = [int(input("Inserisci l'anno attuale: ")), int(input("Mese attuale: ")), int(input("Giorno oggi: "))]

anni = oggi[0] - nascita[0]
if ((nascita[1] == oggi[1]) and (nascita[2] > oggi[2])) or (nascita[1] > oggi[1]):
	anni -= 1

print(f"La tua età è {anni}")