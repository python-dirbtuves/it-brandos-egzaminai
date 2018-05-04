Šokiai
======

.. default-role:: math

Konkurso „Linksmieji šokiai“ dalyvius vertina dvi skirtingos teisėjų komandos,
kurių viena rašo balus tik už techniką, o kita tik už artistiškumą.

**Parašykite programą**, kuri suskaičiuotų, kiek kuri dalyvių pora gavo balų:

- skaičiuojant balų sumą už techniką, atmetamas vienas didžiausias ir vienas
  mažiausias įvertinimas;

- skaičiuojant balų sumą už artistiškumą, atmetamas vienas didžiausias ir
  vienas mažiausias įvertinimas;

- skaičiuojama bendra už techniką ir artistiškumą likusių balų suma.

Rezultatai turi būti pateikti surinktų balų bendros sumos mažėjimo tvarka.

Kai visi vienos teisėjų komandos vertinimai vienodi, atmetami du įvertinimai.

**Duomenys**

Duomenys surašyti tekstiniame faile ``U2.txt``. Visi skaičiai yra sveikojo
tipo.

- Pirmoje eilutėje pateikiamas dalyvių porų skaičius `n\ (1 \leq n \leq 100)`,
  teisėjų, vertinančių techniką, skaičius `k\ (3 \leq k \leq 10)` ir teisėjų,
  vertinančių artistiškumą, skaičius `m\ (3 \leq m \leq 10)`.

- Kitose eilutėse surašyti kiekvienos dalyvių poros įvertinimai balais.
  Kiekvienai dalyvių porai faile skirtos trys eilutės: pirmoje eilutėje yra
  poroje šokančių vardai (pirmos 20 pozicijų), antroje – įvertinimai už
  techniką, o trečioje – įvertinimai už artistiškumą.

**Rezultatai**

Rezultatus spausdinkite tekstiniame faile ``U2rez.txt``.

Faile spausdinkite dalyvių porų sąrašą jų surinktų balų mažėjimo tvarka.
Kiekvienoje eilutėje pirmose **20** pozicijų spausdinkite dalyvių poros vardus,
toliau vieną tarpo simbolį ir tos dalyvių poros bendrą surinktų balų sumą.

**Nurodymai**

- Rašydami programą būtinai panaudokite įrašo duomenų tipą ir masyvus su įrašo
  tipo elementais.

- Parašykite procedūrą duomenims skaityti.

- Parašykite procedūrą dalyvių porų sąrašui rikiuoti gautų balų didėjimo
  tvarka.

- Parašykite funkciją, skaičiuojančią dalyvių poros gautus balus vienam teisėjų
  balų rinkiniui (pvz., už techniką), ir ją panaudokite du kartus: skaičiuodami
  poros balus, gautus už techniką ir už artistiškumą atskirai.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu. 

**Pavyzdys**

``U1.txt``::

  5 5 6
  Petras Rasa
  3 1 5 8 10
  5 6 7 8 9 3
  Rita Jurgis
  6 5 8 5 8
  9 8 7 6 5 8
  Rasa Linas
  10 10 10 10 10
  8 8 8 8 8 8
  Jurgita Matas
  8 8 8 7 7
  9 8 9 8 9 10
  Algis Lina
  7 8 9 10 10
  4 4 5 5 5 7

``U1rez.txt``::

  Rasa Linas           62
  Jurgita Matas        58
  Rita Jurgis          48
  Algis Lina           46
  Petras Rasa          42
