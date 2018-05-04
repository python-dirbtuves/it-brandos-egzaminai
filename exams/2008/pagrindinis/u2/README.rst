Transportas
===========

.. default-role:: math

Vilniuje yra `n` stotelių, kuriose sustoja miesto transporto troleibusai.
Troleibusų maršrutai numeruojami sveikaisiais skaičiais, tačiau nebūtinai iš
eilės. Kiekvienoje stotelėje yra informacinė lentelė, kurioje surašyti
maršrutų, kurių troleibusai sustoja toje stotelėje, numeriai nebūtinai didėjimo
tvarka. Maršruto ilgis nusakomas stotelių skaičiumi.

**Duomenys** yra tekstiniame faile ``U2.txt``. Pirmoje eilutėje yra stotelių
skaičius mieste `n\ (1 \leq n \leq 100)`. Toliau kiekvienoje eilutė je yra
duomenys apie konkrečią stotelę: pavadinimas (20 simbolių), informacinėje
lentelėje esančių maršrutų numerių skaičius irmaršrutų numeriai.

**Parašykite programą**, kuri į tekstinio failo ``U2rez.txt`` pirmą ją eilutę
spausdintų ilgiausio maršruto numerį, jeigu yra keli tokie maršrutai, tuomet iš
jų mažiausią numerį. Toliau spausdintų surasto ilgiausio maršruto stotelių
pavadinimus po vieną eilutė je tokia tvarka, kokia stotelės buvo išvardytos
duomenų faile.

**Nurodymai**:

- Rašydami programą naudokite masyvus su įrašo tipo elementais; papildomai gali
  būti naudojami ir kitokio tipo masyvai.

- Programoje neturi būti sakinių, skirtų darbui su ekranu.

- Parašykite procedūrą, skirtą tik duomenims skaityti iš failo.

- Parašykite funkciją ilgiausio maršruto numeriui rasti.

- Parašykite procedūrą, kuri spausdintų į tekstinį failą nurodyto maršruto
  stotelių pavadinimus. 

**Pavyzdys**:

``U2.txt``::

  5
  Rytas                5 1 2 5 4 6
  Vakarai              3 12 5 4
  Baltasis lokys       6 12 1 6 8 7 3
  Panerys              1 12
  Rudasis tiltas       3 8 14 4

``U2rez.txt``::

  4
  Rytas
  Vakarai
  Rudasis tiltas
