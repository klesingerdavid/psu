1) Zadatak

non_func - stvarna funkcija f(x)
add_noise - šum ε (mjerni podaci)
x, y_measured - skup podataka
podjela na train/test - učenje i provjera modela
LinearRegression() - linearni model
fit() - učenje parametara (θ₀, θ₁)
predict() - predikcija
mean_squared_error - mjera pogreške (MSE)

2) Zadatak
U zadatku 1 koristi se jednostavna linearna regresija (pravac) - model je prejednostavan - lošije prati podatke (underfitting).
U ovom zadatku koristi se polinomska regresija (do stupnja 15) - model je fleksibilniji - puno bolje prati nelinearnu funkciju.

Rezultat:
manji MSE (bolja točnost)
model se puno bolje poklapa sa stvarnom funkcijom

Razlika:
zadatak 1 - pravac
zadatak 2 - zakrivljena krivulja (polinom)

3) Zadatak
MSEtrain - pogreška na train skupu za degree = 2, 6, 15
MSEtest - pogreška na test skupu za iste stupnjeve
jedan graf - prikaz:
stvarne funkcije
modela za degree 2, 6 i 15

degree = 2
- model prejednostavan - underfitting
- veliki MSEtrain i MSEtest

degree = 6
- najbolji balans
- najmanji MSEtest

degree = 15
- model prekompleksan - overfitting
- mali MSEtrain, ali veći MSEtest

Više uzoraka:
model (čak i degree 15) bolje generalizira
MSEtest se smanjuje
overfitting se smanjuje

Manje uzoraka:
model lako zapamti podatke - overfitting
posebno za degree 15:
MSEtrain jako mali
MSEtest jako velik

4) Zadatak

4.1. U datasetu je dostupno 6699 automobila.

4.2. Tipovi stupaca:

name – object

year – int64

selling_price – float64

km_driven – int64

fuel – object

seller_type – object

transmission – object

owner – object

mileage – float64

engine – int64

max_power – float64

seats – int64

4.3. Najveću cijenu ima BMW X7 xDrive 30d DPE, a najmanju Maruti 800 AC.

4.4. 2012. godine proizvedeno je 575 automobila.

4.5. Najviše kilometara ima Maruti Wagon R LXI Minor (577414 km), a najmanje Maruti Eeco 5 STR With AC Plus HTR CNG (1 km).

4.6. Automobili najčešće imaju 5 sjedala.

4.7. Prosječna kilometraža:

Dizel: 88039.97 km

Benzin: 54101.88 km