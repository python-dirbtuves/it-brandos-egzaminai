Šokiai
======

.. default-role:: math

Konkurso „Linksmieji šokiai“ dalyvius vertina teisėjų komanda, kuri rašo balus
už techniką ir už artistiškumą.

**Parašykite programą**, kuri suskaičiuotų, kiek kuri dalyvių pora gavo balų:

- jei skaičiuojant balų sumą už techniką, atmetamas vienas didžiausias ir
  vienas mažiausias į vertinimas;

- jei skaičiuojant balų sumą už artistiškumą, atmetamas vienas didžiausias ir
  vienas mažiausias įvertinimas;

- skaičiuojama bendra už techniką ir artistiškumą likusių balų suma.

Rezultatai turi būti pateikti surinktų balų bendros sumos mažė jimo tvarka.

Kai visi vertinimai už techniką (artistiškumą) vienodi, atmetami du
įvertinimai.

**Duomenys**

Duomenys surašyti tekstiniame faile ``U2.txt``. Visi skaičiai yra sveikojo
tipo.

- Pirmoje eilutėje pateikiamas šokėjų skaičius `n\ (1 \leq n \leq 100)` ir
  teisėjų skaičius `k\ (3 \leq k \leq 10)`.

- Kitose eilutėse yra surašyti kiekvienos šokėjų poros įvertinimai balais.
  Kiekvienai porai faile skirtos trys eilutės: pirmoje iš jų eilutėje yra
  poroje šokančių vardai (pirmos 20 pozicijų), antroje – įvertinimai už
  techniką, o trečioje – įvertinimai už artistiškumą.

**Rezultatai**

Rezultatus spausdinkite tekstiniame faile ``U2rez.txt``.

Faile spausdinkite šokėjų porų sąrašą jų surinktų balų mažėjimo tvarka.
Kiekvienoje eilutėje pirmose 20 pozicijų spausdinkite šokėjų poros vardus,
toliau vieną tarpo simbolį ir tos šokėjų poros bendrą surinktų balų sumą.

**Nurodymai**

- Rašydami programą būtinai panaudokite įrašo duomenų tipą ir masyvus su įrašo
  tipo elementais.

- Parašykite procedūrą duomenims skaityti.

- Parašykite procedūrą šokėjų sąrašui rikiuoti gautų balų mažėjimo tvarka.

- Parašykite funkciją, skaičiuojančią šokėjų poros gautus balus vienam teisėjų
  balų rinkiniui (pvz., už techniką), ir ją panaudokite du kartus: skaičiuodami
  poros balus, gautus už techniką ir už artistiškumą atskirai.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu. 

**Pavyzdys**

``U2.txt``::

  5 5
  Petras Rasa
  3 1 5 8 10
  5 6 7 8 9
  Rita Jurgis
  6 5 8 5 8
  9 8 7 6 5
  Rasa Linas
  10 10 10 10 10
  8 8 8 8 8

``U2rez.txt``::

  Rasa Linas           54
  Rita Jurgis          40
  Petras Rasa          37
