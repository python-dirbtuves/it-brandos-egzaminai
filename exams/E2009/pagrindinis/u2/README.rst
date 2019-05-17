Varžybos
========

.. default-role:: math

800 metrų bėgimo varžyboms registravosi `n\ (2 \leq n \leq 50)` bėgikų.
Stadione yra 8 bėgimo takeliai. Sportininkai atsitiktinai suskirstyti į `k`
grupių taip, kad grupėje būtų ne mažiau kaip du bė gikai.

**Parašykite programą**, kuri iš kiekvienos grupės atrinktų pusę bėgikų,
pasiekusių geriausius rezultatus. Jeigu grupėje yra nelyginis skaičius bėgikų,
tada atrenkama vienu sportininku mažiau (pvz., iš penkių bėgikų atrenkami du
pasiekusieji geriausius rezultatus). Žinoma, kad **visi** sportininkų pasiekti
rezultatai yra **skirtingi**.

**Duomenys** pateikiami tekstiniame faile ``U2.txt``. Pirmoje failo eilutė je
nurodomas bėgikų grupių skaičius `k`. Toliau iš eilės pateikiami visų bėgikų
grupių sąrašai tokia tvarka:

- pirmoje sąrašo eilutėje pateikiamas bėgikų skaičius grupėje;

- toliau – kiekvieno bėgiko vardas bei pavardė (skiriamos pirmosios 20
  pozicijų) ir rezultatas (minutės, sekundės). Vieno sportininko duomenims
  skiriama viena eilutė.

**Rezultatai** pateikiami tekstiniame faile ``U2rez.txt``. Spausdinamas visų
atrinktų bėgikų sąrašas pasiekto rezultato laiko didėjimo tvarka. Vieno bėgiko
duomenims skiriama viena eilutė: vardas bei pavardė (skiriamos pirmosios 20
pozicijų) ir rezultatas (minutės ir sekundės, atskirtos vienu tarpu). 

**Pavyzdžiai**:

``U2.txt``::

  3
  4
  Katinas Batuotas     4 25
  Katinas Ratuotas     3 59
  Katinas Rainas       4 15
  Katinas Jaunas       6 20
  2
  Katinas Rudas        6 45
  Katinas Juodas       3 55
  5
  Katinas Baltas       3 58
  Katinas Gauruotas    4 2
  Katinas Plikas       4 5
  Katinas Ilgas        4 4
  Katinas Trumpas      4 6

``U2rez.txt``::

  Katinas Juodas       3 55
  Katinas Baltas       3 58
  Katinas Ratuotas     3 59
  Katinas Gauruotas    4 2
  Katinas Rainas       4 15

**Nurodymai**: 

- Programoje būtinai naudokite masyvus su įrašo tipo elementais; papildomai
  galite naudoti kitų tipų masyvus.

- Programoje neturi būti sakinių, skirtų darbui su ekranu.

- Parašykite procedūrą, kuri rezultatus pateikia tekstiniame faile.
