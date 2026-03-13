ime = input("Ime datoteke: ")

try:
    dat = open(ime)
except:
    print("Datoteka ne postoji")
    exit()

suma = 0
broj = 0

for linija in dat:
    if linija.startswith("X-DSPAM-Confidence:"):
        dio = linija.split(":")
        #split razbija u vise stringova
        vrijednost = float(dio[1])
        suma = suma + vrijednost
        broj = broj + 1

prosjek = suma / broj
print("Average X-DSPAM-Confidence:", prosjek)