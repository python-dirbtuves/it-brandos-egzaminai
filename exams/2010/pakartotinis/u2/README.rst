Gimtadienis
===========

.. default-role:: math

Viktorija savo gimtadienio proga užsakė pietus visai klasei. Kiekvienas svečias
renkasi patiekalus iš pateikto meniu sąrašo. Parašykite programą, kuri
suskaičiuotų už kokią sumą patiekalų pasirinko kiekvienas svečias ir kiek iš
viso kainuos gimtadienio puota.

**Duomenys**

Duomenys surašyti tekstiniame faile ``U2.txt``. Visi skaičiai yra sveikojo
tipo.

- Pirmoje eilutė je pateikiamas gimtadienio meniu visų patiekalų skaičius `P\
  (1 \leq P \leq 30)`.

- Antroje eilutė je pateikiamos meniu visų patiekalų kainos centais.

- Trečioje eilutė je pateikiamas svečių skaičius `N\ (1 \leq N \leq 100)`.

- Tolesnė se `N` eilučių pateikiami svečių užsakymai. Vieno svečio duomenys
  užrašyti atskiroje eilutėje: vardas (pirmos 15 pozicijų) ir pasirinktų
  patiekalų sąrašas. Svečio pasirinkti patiekalai išdėsyti tokia pat tvarka
  kaip ir kainų sąraše: skaičių yra tiek, kiek patiekalų sąraše. Jeigu svečias
  kurio nors patiekalo nesirinko, toje vietoje rašomas nulis.

Pavyzdžiui, duomenų failo pavyzdyje Petras pasirinko:

- vieną pirmą patiekalą;

- vieną antrą patiekalą;

- trečio patiekalo nesirinko;

- ketvirto patiekalo nesirinko;

- du penktus patiekalus;

- vieną šeštą patiekalą;

- septinto patiekalo nesirinko;

- aštunto patiekalo nesirinko;

- keturis devintus patiekalus;

- penkis dešimtus patiekalus.

**Rezultatai**

Rezultatai pateikiami tekstiniame faile ``U2rez.txt``.

- Pirmose `N` eilučių pateikiami duomenys apie kiekvieną svečią atskiroje
  eilutėje: svečio vardas ir kiek iš viso kainuos jo pietūs centais. Vardą (jis
  sudarytas iš 15 simbolių) nuo kainos reikia skirti vienu tarpu.

- Paskutinėje eilutėje pateikiama, kiek iš viso Viktorijai kainuos gimtadienio
  puota. Pateikiami du skaičiai: kiek litų ir kiek centų. Skaičius skirti vienu
  tarpu.

**Pavyzdžiai**

``U2.txt``::

  10
  12 25 35 2 3 9 45 12 3 2
  5
  Petras         1 1 0 0 2 1 0 0 4 5
  Rasa           2 3 2 1 0 5 1 1 1 12
  Linas          0 0 1 13 1 0 1 0 1 0
  Jurgutis       0 0 2 5 5 1 0 1 0 1
  Liepa          1 2 1 1 1 1 1 1 1 1

``U2rez.txt``::

  Petras          74
  Rasa            300
  Linas           112
  Jurgutis        118
  Liepa           173
  7 77

**Nurodymai**

- Programoje **būtinai** naudokite įrašo duomenų tipą ir masyvus su įrašo tipo
  elementais.

- Parašykite funkciją, kuri suskaičiuotų, kiek iš viso kainuos vieno svečio
  užsakytų patiekalų kaina centais.

- Parašykite funkciją, kuri suskaičiuotų, kiek iš viso kainuos gimtadienio
  puota centais.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu. 
