Amžius
======

.. default-role:: math

Turime žmonių gyvenimo datas: gimimo ir mirties. Reikia parašyti programą, kuri
suskaičiuotų kiekvieno žmogaus gyvenimo trukmę dienomis.

**Duomenys**. Tekstiniame faile ``U2.txt`` pirmoje eilutėje yra žmonių skaičius
`N\ (1 \leq N \leq 100)`. Kitose `N` eilučių yra duomenys apie žmones: vardas
ir pavardė (pirmos 25 pozicijos, tekstas rašomas pradedant pirmąja pozicija),
po to yra šeši skaičiai: gimimo data (metai, mėnuo, diena) ir mirties data
(metai, mėnuo, diena).

**Rezultatai**. Tekstiniame faile ``U2rez.txt`` reikia pateikti žmonių sąrašą:
vardas ir pavardė (pirmos 25 pozicijos, kaip ir duomenų faile), po to septyni
skaičiai: gimimo data, mirties data, gyvenimo trukmė dienomis. Skaičius
skirkite vienu tarpo simboliu.

**Pastabos**. Rašydami programą laikykite, kad ilgiausiai gyvenusio žmogaus
amžius gali būti 125 metai. Skaičiuodami darykite prielaidą, kad vasario mėnuo
visada turi 28 dienas. Jeigu žmogus gimė ir mirė tą pačią dieną, jo gyvenimo
trukmė yra nulis (0) dienų.

**Nurodymai**:

- Rašydami programą naudokite įrašo tipo kintamuosius ir masyvus su įrašo tipo
  elementais.

- Programoje neturi būti sakinių, skirtų darbui su ekranu.

- Parašykite procedūrą, skirtą **tik** duomenims iš failo skaityti.

- Parašykite procedūrą, skirtą **tik** sąrašui spausdinti rezultatų faile.

- Parašykite funkciją žmogaus gyvenimo trukmei dienomis skaičiuoti, kai žinomos
  žmogaus gimimo ir mirties datos.

**Pavyzdys**:

``U2.txt``::

  8
  Albertas Einšteinas      1879 03 14 1955 04 18
  Balys Sruoga             1896 02 02 1947 10 16
  Antanas Vienuolis        1882 04 07 1957 08 17
  Ernestas Rezerfordas     1871 08 30 1937 10 17
  Nilsas Boras             1885 10 07 1962 11 18
  Nežiniukas Pirmasis         8 05 24    8 05 25
  Nežiniukas Antrasis       888 05 25  888 05 25
  Nežiniukas Trečiasis        1 01 01  125 01 01

``U2rez.txt``::

  Albertas Einšteinas      1879 3 14 1955 4 18 27775
  Balys Sruoga             1896 2 2 1947 10 16 18871
  Antanas Vienuolis        1882 4 7 1957 8 17 27507
  Ernestas Rezerfordas     1871 8 30 1937 10 17 24138
  Nilsas Boras             1885 10 7 1962 11 18 28147
  Nežiniukas Pirmasis      8 5 24 8 5 25 1
  Nežiniukas Antrasis      888 5 25 888 5 25 0
  Nežiniukas Trečiasis     1 1 1 125 1 1 45260       
