Gimtadienis
===========

.. default-role:: math

Martynas savo gimtadienio proga užsakė pietus visai klasei. Pietus sudaro
vienodas patiekalų komplektas kiekvienam svečiui. Žinoma, kiek ir kokių
produktų reikia kiekvienam patiekalui pagaminti ir kiek kuris produktas
kainuoja.

**Parašykite programą**, kuri suskaičiuotų, kiek kainuos **kiekvienas
patiekalas** ir kiek kainuos **vieno svečio** pietūs.

**Duomenys**

Duomenys surašyti tekstiniame faile ``U2.txt``. Visi skaičiai yra sveikojo
tipo.

- Pirmoje eilutė je pateikiamas visų produktų, reikalingų patiekalams gaminti,
  skaičius `N\ (1 \leq N \leq 10)` ir pietų komplekto patiekalų skaičius `P\ (1
  \leq P \leq 12)`.

- Antroje eilutė je pateikiamos visų produktų kiekio vienetų kainos centais.

- Toliau atskirose `P` eilučių pateikiami duomenys apie patiekalus: patiekalo
  pavadinimas (pirmos 15 pozicijų) ir produktų, reikalingų patiekalui
  pagaminti, kiekių sąrašas. Patiekalų sąraše produktai išdėstyti tokia pat
  tvarka, kaip ir kainų sąraše. Jeigu kuris nors produktas nenaudojamas,
  rašomas nulis.

Pavyzdžiui, duomenų faile užrašas ``Salotos 5 1 0 0 2 1`` reiškia, kad salotoms
pagaminti reikia keturių produktų (galėtų būti pomidorai, svogūnai, grietinė ir
druska):

- pirmo produkto, kurio kiekio vieneto kaina 12 centų, reikia 5 kiekio vienetų,

- antro produkto, kurio kiekio vieneto kaina 25 centai, reikia 1 kiekio
  vieneto,

- trečio ir ketvirto produktų nereikia,

- penkto produkto, kurio kiekio vieneto kaina 3 centai, reikia 2 kiekio
  vienetų,

- šešto produkto, kurio kiekio vieneto kaina 9 centai, reikia 1 kiekio vieneto.

**Rezultatai**

Rezultatai pateikiami tekstiniame faile ``U2rez.txt``.

- Pirmose `P` eilučių reikia išvardyti visus patiekalus po vieną eilutėje:
  patiekalo pavadinimas ir kiek tas patiekalas kainuos centais. Pavadinimą (jam
  skirta 15 simbolių) nuo kainos reikia skirti vienu tarpu.

- Paskutinėje eilutėje reikia parašyti, kiek iš viso kainuos vieno svečio
  pietūs. (Turi būti išspausdinti du skaičiai: kiek litų ir kiek centų,
  atskirti vienu tarpu.)

**Pavyzdys**

``U2.txt``::

  6 5
  12 25 35 2 3 9
  Salotos         5 1  0  0 2 1
  Kepsnys         6 3 12  9 0 0
  Gaiva           0 0  1 15 1 0
  Ledai Miau      0 0  5  5 5 1
  Tortas          1 2  1  1 1 1

``U2rez.txt``::

  Salotos         100
  Kepsnys         585
  Gaiva           68
  Ledai Miau      209
  Tortas          111
  10 73

**Nurodymai**

- Programoje **būtinai** naudokite įrašo duomenų tipą ir masyvus su įrašo tipo
  elementais.

- Parašykite funkciją, kuri suskaičiuotų vieno patiekalo kainą centais.

- Parašykite funkciją, kuri suskaičiuotų vieno svečio pietų kainą centais.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu. 
