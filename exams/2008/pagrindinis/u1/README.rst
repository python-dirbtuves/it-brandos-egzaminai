Tyrimas
=======

.. default-role:: math

Ukmergėje yra `m\ (1 \leq m \leq 100)` autobusų maršrutų. Norėdami
išsiaiškinti, kiek autobusų reikia kiekvienam maršrutui, mokiniai skaičiavo,
kiek pervežama keleivių. Stebėtoju vienoje stotelėje dirbo tik vienas mokinys.
Mokiniai stebėjo (dirbo) visose miesto stotelėse, išskyrus paskutinę kiekvieno
maršruto stotelę, kurioje išlipa visi dar važiavę keleiviai. Buvo registruojami
visų maršrutų keleiviai. Savo stebėjimo rezultatus kiekvienas mokinys rašė
duomenų lape: maršruto numerį ir kiek įlipo keleivių (teigiamas skaičius)
arba/ir maršruto numerį ir kiek išlipo keleivių (neigiamas skaičius). Atvejai,
kai stotelėje nebuvo įlipusių ir/arba išlipusių keleivių, duomenų lape nebuvo
registruojami. (Žiūrėkite Aidos duomenų lapo pavyzdį).

Stebėtoja Aida

+-----------+--------------+
| Maršrutas | Įlipo/išlipo |
+-----------+--------------+
| 6         | -5           |
+-----------+--------------+
| 6         | 12           |
+-----------+--------------+
| 1         | 4            |
+-----------+--------------+
| 6         | 1            |
+-----------+--------------+
| 6         | 2            |
+-----------+--------------+

**Duomenys**. Visi stebėjimų duomenys surašyti tekstiniame faile ``U1.txt``.
Pirmoje eilutėje yra visų mokinių surinktų duomenų skaičius `n\ (n \leq 1)`.
Tolesnėse `n` eilučių yra po du skaičius: maršruto numeris ir keleivių skaičius
(teigiamas, jeigu įlipo, neigiamas – jeigu išlipo).

**Parašykite programą**, kuri spausdintų faile ``U1rez.txt`` mokinių stebėjimų
rezultatus.

1. Pirmoje eilutėje spausdintų maršrutų, kuriais važiavo bent vienas keleivis,
   numerius didėjimo tvarka.

2. Antroje eilutėje spausdintų, kiek keleivių vežta kiekvienu maršrutu maršrutų
   numerių didėjimo tvarka.

3. Trečioje eilutėje spausdintų kiek kiekvieno maršruto autobusų keleivių
   išlipo visose tarpinėse stotelėse arba nulį, jeigu nė vienas keleivis iš to
   maršruto autobusų neišlipo. Spausdintų maršrutų numerių didėjimo tvarka.

4. Ketvirtoje eilutėje spausdintų maršruto, kurio visais autobusais vežta
   daugiausia keleivių, numerį. Jeigu tokie maršrutai yra keli, tai spausdintų
   mažiausią numerį.

Kiekvienam skaičiui spausdinti skirtos 6 pozicijos.

**Pastaba**. Vežtų maršrutu keleivių skaičius yra lygus į lipusių į visus to
maršruto autobusus keleivių skaičių sumai.

**Nurodymai**:

- Rašydami programą naudokite tik vienmačius sveikųjų skaičių masyvus.

- Programoje neturi būti sakinių, skirtų darbui su ekranu.

- Rezultatų faile turi būti keturios eilutės. Jeigu ne visi skaičiavimai
  atlikti, tuomet atitinkamoje eilutėje spausdinkite žodį ``NE``.

- Parašykite procedūrą duomenims iš failo skaityti.

- Parašykite procedūrą tik maršrutų numeriams spausdinti didėjimo tvarka.

- Parašykite funkciją maršruto, kuriuo vežta daugiausia keleivių, numeriui rasti.

**Pavyzdžiai**:

``U1.txt``::

  12
  6 -1
  6  5
  3 15
  4 9
  6 -2
  12 16
  8 45
  4 -5
  3 12
  3 -10
  12 -16
  9 9

``U1rez.txt``::

     3     4     6     8     9    12
    27     9     5    45     9    16
   -10    -5    -3     0     0   -16
     8
