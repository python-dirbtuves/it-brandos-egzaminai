Varžybos
========

.. default-role:: math

100 metrų plaukimo varžyboms registravosi `n\ (5 \leq n \leq 50)` sportininkų.
Baseine yra 5 plaukimo takeliai. Sportininkai atsitiktinai buvo suskirstyti į
`k` grupių taip, kad grupėje būtų ne mažiau kaip du plaukikai.

**Parašykite programą**, kuri finalui atrinktų 5 plaukikus, pasiekusius
geriausių rezultatų. Žinoma, kad **visų** sportininkų rezultatai yra
**skirtingi**.

**Duomenys** pateikiami tekstiniame faile ``U2.txt``. Pirmoje eilutė je
nurodomas plaukikų grupių skaičius `k`. Toliau iš eilės pateikiami visų
plaukikų grupių sąrašai tokia tvarka:

- pirmoje sąrašo eilutėje pateikiamas plaukikų skaičius grupėje;

- toliau – kiekvieno plaukiko vardas bei pavardė (skiriamos pirmosios 20
  pozicijų) ir rezultatas (minutės ir sekundės). Vieno sportininko duomenims
  skiriama viena eilutė.

**Rezultatai** pateikiami tekstiniame faile ``U2rez.txt``. Spausdinamas penkių
atrinktų plaukikų sąrašas pasiekto rezultato laiko didėjimo tvarka. Vieno
plaukiko duomenims skiriama viena eilutė: vardas bei pavardė (skiriamos
pirmosios 20 pozicijų) ir rezultatas (minutės ir sekundės, atskirtos vienu
tarpu). 

**Pavyzdžiai**:

``U2.txt``::

  3
  3
  Lokys Baltasis      4 25
  Lokys Rudasis       3 59
  Lokys Juodasis      4 15
  2
  Vilkas Pilkas       6 45
  Vilkas Baltas       3 55
  5
  Lapinas Rudas       3 58
  Lapinas Baltas      4 2
  Lapinas Gudrutis    4 5
  Lapinas Ilgas       4 4
  Lapinas Trumpas     4 4

``U2rez.txt``::

  Vilkas Baltas       3 55
  Lapinas Rudas       3 58
  Lokys Rudasis       3 59
  Lapinas Baltas      4 2
  Lapinas Ilgas       4 4

**Nurodymai**: 

- Programoje būtinai naudokite masyvus su įrašo tipo elementais; papildomai
  galite naudoti kitų tipų masyvus.

- Programoje neturi būti sakinių, skirtų darbui su ekranu.

- Parašykite procedūrą, skirtą sportininkų sąrašui rikiuoti.

- Parašykite procedūrą, kuri rezultatus pateikia tekstiniame faile. 
