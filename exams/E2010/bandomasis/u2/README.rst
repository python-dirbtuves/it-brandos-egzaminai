Pasirinkimas
============

.. default-role:: math

Abiturientas sudarė jį dominančių valstybių aukštųjų mokyklų sąrašą.

**Parašykite programą**, kuri išrinktų po vieną aukščiausią reitingą turinčią
kiekvienos valstybės aukštąją mokyklą ir gautą sąrašą surikiuotų reitingų
mažėjimo tvarka.

**Duomenys** pateikiami tekstiniame faile ``P2.txt``. Pirmoje failo eilutėje
nurodomas valstybių skaičius `N\ (1 \leq N \leq 100)`. Toliau pateikiami
valstybių sąrašai tokia tvarka:

- pirmoje sąrašo eilutėje užrašomas valstybės pavadinimas (pirmosios 15
  pozicijų) ir aukštųjų mokyklų skaičius;

- toliau atskirose eilutėse pateikiami duomenys apie mokyklą: pavadinimas
  (pirmosios 30 pozicijų) ir reitingas (sveikasis skaičius).

**Rezultatai** pateikiami tekstiniame faile ``P2rez.txt``. Spausdinamas
atrinktų aukštųjų mokyklų sąrašas reitingų mažėjimo tvarka: valstybė, aukštoji
mokykla, reitingas. Reikšmės viena nuo kitos atskiriamos vienu tarpu.

**Nurodymai**

- Programoje būtinai naudokite įrašo duomenų tipą ir masyvus su įrašo tipo
  elementais.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

- Parašykite procedūrą, kuri rikiuotų sąrašą reitingų mažėjimo tvarka. 

**Pavyzdys**

``P2.txt``::

  4
  Gailuva         3
  Dubysos universitetas          45
  Petro universitetas            55
  Baltijos kolegija              9
  Bambukija       1
  Bambuko muzikos akademija      35
  Guglija         2
  Medienos apdorojimo kolegija   14
  Turizmo kolegija               13
  Baltieji lokiai 4
  Baltasis universitetas         10
  Pilkasis universitetas         15
  Rudoji kolegija                8
  Spalvos kolegija               99

``P2rez.txt``::

  Baltieji lokiai Spalvos kolegija               99
  Gailuva         Petro universitetas            55
  Bambukija       Bambuko muzikos akademija      35
  Guglija         Medienos apdorojimo kolegija   14
