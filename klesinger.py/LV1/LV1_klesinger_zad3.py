'''Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
ispiše odgovarajuću poruku. tuple'''

brojevi = []

while True:
    unos = input("Unesite broj (upišite Done za kraj): ")

    if unos == "Done":
        break

    try:
        broj = float(unos)
        brojevi.append(broj)
    except:
        print("Pogresan unos, unesite broj")

if len(brojevi) == 0:
    print("Niste unijeli nijedan broj.")
else:

    print("Broj unesenih brojeva:", len(brojevi))

    srednja = sum(brojevi) / len(brojevi)
    #len(brojevi) vraća koliko elemenata (brojeva) se nalazi u listi brojevi
    print("Srednja vrijednost:", srednja)

    print("Minimalna vrijednost:", min(brojevi))
    print("Maksimalna vrijednost:", max(brojevi))

    brojevi.sort()

    print("Sortirana lista:", brojevi)