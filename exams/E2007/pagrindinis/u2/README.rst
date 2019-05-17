Grybautojai
===========

.. default-role:: math

Susibūrė grybautojų mėgėjų grupė. Kiekvienas dalyvis, grįžęs iš miško, užrašo,
kiek rado baravykų, raudonikių ir lepšių.

Parašykite programą, kuri skaičiuotų, kiek kiekvienas grybautojas per sezoną
rado atskirai baravykų, raudonikių bei lepšių ir kuris grybautojas surinko
daugiausia grybų ir kiek jų surinko.

**Pradiniai duomenys** surašyti į tekstinį failą ``U2.txt``. Pirmoje eilutėje
įrašytas grybautojų skaičius `(1 \leq n \leq 100)`. Tolesnėse eilutėse
pateikiami duomenys apie kiekvieno grybautojo surinktus grybus. Viena eilutė
skiriama grybautojo vardui (pirmos 15 eilutės pozicijų) ir jo grybautų dienų
skaičiui `d\ (1 \leq d \leq 50)` nurodyti. Tolesnės `d` eilučių skiriamos to
grybautojo kiekvienos dienos surinktiems grybams nurodyti: viena eilutė –
vienai dienai, kiekvienoje eilutėje yra po tris sveikuosius skaičius – baravykų
skaičius, raudonikių skaičius ir lepšių skaičius. Po to ta pačia tvarka
pateikiami kitų grybautojų duomenys.

**Rezultatai** turi būti įrašomi į tekstinį failą ``U2rez.txt``. Čia
kiekvienoje eilutėje nuo pradžios spausdinamas grybautojo vardas, toliau
spausdinami jo surinktų per sezoną grybų skaičiai – baravykų, raudonikių ir
lepšių. Grybautojo vardui skirkite 15 pirmų pozicijų, spausdinkite nuo eilutės
pradžios. Toliau spausdinkite grybų skaičius (kiekvienam skirkite po 5
pozicijas). Failo gale atskira eilute spausdinkite daugiausia grybų surinkusio
grybautojo vardą ir jo surinktų per sezoną grybų skaičių. Jeigu yra keli tokie
grybautojai, tada spausdinkite pirmesnį pagal pradinių duomenų sąrašą.

**Nurodymai**:

- Duomenims ir rezultatams apdoroti naudokite įrašo tipo kintamuosius ir
  masyvus su įrašo tipo elementais.

- Duomenims skaityti iš failo parašykite procedūrą. Duomenų nebūtina laikyti
  pradiniu pavidalu.

- Parašykite procedūrą rezultatams (kas, kokių ir kiek surinko grybų)
  spausdinti.

- Parašykite funkciją geriausiam grybautojui (radusiam daugiausia grybų) rasti.

- Programoje neturi būti sakinių, skirtų darbui su ekranu. 
 
**Pavyzdys**:

``U2.txt``::

  4
  Petras        3
  5 13 8
  4 0  5
  16 1 0
  Algis         1
  9 6 13
  Jurgis        4
  4 14 2
  4 4  15
  16 15 251
  1  2  3
  Rita          2
  6 65 4
  4 4  13

``U2.txt``::

  Petras          25   14   13
  Algis            9    6   13
  Jurgis          25   35  271
  Rita            10   69   17
  Jurgis         331
