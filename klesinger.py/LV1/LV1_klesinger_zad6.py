ham_rijeci = 0
ham_broj = 0
spam_rijeci = 0
spam_broj = 0
spam_usklicnik = 0

dat = open("SMSSpamCollection.txt")

for linija in dat:
    linija = linija.strip()
    dijelovi = linija.split()
    tip = dijelovi[0]
    poruka = dijelovi[1:]
    broj_rijeci = len(poruka)

    if tip == "ham":
        ham_rijeci = ham_rijeci + broj_rijeci
        ham_broj = ham_broj + 1
    elif tip == "spam":
        spam_rijeci = spam_rijeci + broj_rijeci
        spam_broj = spam_broj + 1
        tekst = " ".join(poruka)
        if tekst.endswith("!"):
            spam_usklicnik = spam_usklicnik + 1

prosjek_ham = ham_rijeci / ham_broj
prosjek_spam = spam_rijeci / spam_broj

print(prosjek_ham)
print(prosjek_spam)
print(spam_usklicnik)