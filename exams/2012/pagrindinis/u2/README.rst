Kauliukai
=========

.. default-role:: math

Olimpo dievai renka pasaulio valdovą mesdami kauliukus. Visi dievai eilės
tvarka meta vienodą kauliukų skaičių. Dievo išmestų kauliukų taškų suma
skaičiuojama taip: lyginiai taškai pridedami, o nelyginiai – atimami.

Valdovu skelbiamas tas, kuris surenka daugiausia taškų:

- jeigu tokių yra ne vienas, tada valdovu bus tas, kuris daugiausia kartų
  išmetė kauliukus su lyginiu skaičiumi taškų;

- jeigu ir tuo atveju yra keli vienodi, tada valdovu bus pirmesnis pagal
  pradinį duomenų sąrašą.

**Parašykite programą**, kuri suskaičiuotų, kuris iš dievų taps pasaulio
valdovu.

**Duomenys**

Duomenys yra tekstiniame faile ``U2.txt``:

- pirmoje eilutėje yra du sveikieji skaičiai: dievų skaičius `n\ (2 \leq n \leq
  50)` ir kauliukų skaičius `k\ (1 \leq k \leq 10)`;

- kitose `n` eilučių yra surašyti dievų mestų kauliukų taškai:

  * pirmose 10 pozicijų, pradedant pirmąja, yra dievo vardas (vienas žodis);

  * po to vienas tarpo simbolis;

  * toliau surašyti išmestų kauliukų taškai, skiriami vienu tarpo simboliu.
    
**Rezultatas**

Tekstiniame faile ``U2Rez.txt`` pirmoje eilutėje spausdinkite valdovo vardą
(visus 10 simbolių, kaip buvo duomenų faile), tarpo simbolį ir jo surinktų
taškų skaičių. Vardą spausdinkite pradėdami pirma pozicija.

**Nurodymai**

- Naudokite įrašo tipo duomenų tipą.

- Parašykite procedūrą duomenims iš failo skaityti.

- Parašykite funkciją, kuri surastų valdovą.

- Nevartokite sakinių, skirtų darbui su ekranu ir klaviatūra. 

**Pavyzdys**

``U2.txt``::

  2 3
  Hermis     6 1 2
  Hera       2 6 6

``U2rez.txt``::

  Hera       14


Šaltinis
--------

http://nec.lt/failai/2730_IT-1-2012.pdf
