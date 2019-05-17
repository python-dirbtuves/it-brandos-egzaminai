Metro
=====

.. default-role:: math

Metro stotyse automatiniai registratoriai skaičiuoja įeinančius ir išeinančius
keleivius. Stotyse yra atskiri įėjimai keleiviams, kurie nori važiuoti
(įeinantys iš gatvės), ir išėjimai keleiviams, kurie atvažiavo (išeinantys į
gatvę). Parašykite programą, kuri atliktų keleivių srautų analizę.

**Duomenys** surašyti tekstiniame faile ``U1.txt``. Miesto metro stotys
sunumeruotos iš eilės pradedant vienetu. Jų yra `n\ (1 \leq n \leq 100)`.
Savaitės dienos numeruojamos nuo pirmadienio iki sekmadienio skaičiais nuo
vieno iki septynių. Kiekvienoje stotyje kiekvieną dieną įėjusių ir išėjusių
keleivių skaičiai yra žinomi, tačiau ne visi duomenys yra surašyti duomenų
faile.

Pirmoje failo eilutėje yra duomenų skaičius `m\ (1 \leq m \leq 1000)`.
Tolesnėse m eilučių yra po 4 sveikuosius skaičius: stoties numeris, dienos
numeris, įėjusių keleivių skaičius, išėjusių keleivių skaičius.

**Rezultatus** spausdinkite tekstiniame faile ``U1rez.txt``.

1. Pirmoje eilutėje spausdinkite duomenų faile surašytų stočių numerius
   didėjimo tvarka.

2. Antroje eilutėje spausdinkite, kiek keleivių apsilankė kiekvienoje stotyje
   (praėjo pro  registratorius) stočių numerių didėjimo tvarka.

3. Trečioje eilutėje spausdinkite stoties, kurioje apsilankė daugiausia
   keleivių per savaitę (įėjusių ir išėjusių keleivių suma), numerį. Jeigu yra
   kelios tokios stotys, tai spausdinkite tą, kurios numeris mažiausias.

4. Ketvirtoje eilutėje spausdinkite, kiek per savaitę iš viso žmonių mieste
   naudojosi metro paslaugomis (įėjusiųjų keleivių skaičius).

Kiekvienam skaičiui spausdinti skirtos 6 pozicijos.

**Nurodymai**

- Rašydami programą naudokite vienmačius sveikųjų skaičių masyvus.

- Programoje neturi būti sakinių, skirtų darbui su ekranu.

- Rezultatų faile turi būti **keturios** eilutės. Jeigu atlikti ne visi
  skaičiavimai, tada atitinkamoje eilutėje spausdinkite žodį NE.

- Parašykite procedūrą **tik** duomenims iš failo skaityti.

- Parašykite procedūrą pirmos rezultatų failo eilutės duomenims spausdinti.

- Parašykite procedūrą antros rezultatų failo eilutės duomenims spausdinti.

- Parašykite funkciją stoties, kurioje per savaitę apsilankė daugiausia
  keleivių, numeriui rasti.

**Pavyzdžiai**

``U1.txt``::

  12
  5 2 225 32
  1 1 125 29
  5 1  14 14
  6 7  25  0
  2 6   0  0
  1 4   0  5
  5 3   3  3
  5 3  25  1
  5 3  22  0
  1 5  22 11
  1 6   2 18
  9 4  12 22

``U1rez.txt``::

     1     2      5      6      9
   212     0    339     25     34
     5
   475
