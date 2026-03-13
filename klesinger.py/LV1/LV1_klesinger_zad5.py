dat = open("song.txt")

rjecnik = {}

for linija in dat:
    rijeci = linija.split()
    for rijec in rijeci:
        if rijec in rjecnik:
            rjecnik[rijec] = rjecnik[rijec] + 1
        else:
            rjecnik[rijec] = 1

jednom = []

for rijec in rjecnik:
    if rjecnik[rijec] == 1:
        jednom.append(rijec)

print("Broj riječi koje se pojavljuju samo jednom:", len(jednom))

for r in jednom:
    print(r)