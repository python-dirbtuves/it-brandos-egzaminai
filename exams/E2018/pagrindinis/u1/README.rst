Vėliavėlės
==========

.. default-role:: math

Darželyje  vaikai  karpė  spalvotas juosteles  ir  kiekvienas  dėliojo  į  savo
krūveles  pagal  spalvas: geltonas  **(G)**, žalias **(Z)**  ir  raudonas
**(R)**. Kai kurie karpė ne vienos spalvos juosteles. Po to visi vaikai iš visų
juostelių klijavo Lietuvos Respublikos vėliavėles – ant kartono pagrindo iš
abiejų pusių priklijavo atitinkamas juosteles. Taigi vienai vėliavėlei reikėjo
dviejų kiekvienos spalvos juostelių. Vaikai karpė nevienodai stropiai, todėl
juostelių galėjo būti skirtingas skaičius.

Parašykite programą, kurisuskaičiuotų:

- kiek buvo suklijuota vėliavėlių, jeigu jų buvo klijuojama tiek, kiek pakako
  juostelių;

- kiek kokios spalvos juostelių liko nepanaudota.

**Pradiniai duomenys**

Duomenys pateikiami tekstiniame faile ``U1.txt``.

Duomenų faile įrašyta:

- Pirmoje eilutėje užrašytas juostelių krūvelių skaičius `n (1 \leq n \leq
  30)`.

- Toliau kiekvienoje iš `n` eilučiųpateikta  informacija  apie  sukarpytas
  juosteles–krūvelės spalva (spalvos kodas: ``G``, ``Z`` arba ``R``) ir tos
  spalvos juostelių skaičius, atskirti vienu tarpo simboliu.

Visi skaičiai yra sveikieji.

RezultataiRezultatuspateikitetekstiniame faile ``U1rez.txt``.

- Pirmoje eilutėje įrašykite, kiek buvo suklijuota vėliavėlių.

- Antroje  eilutėje  įrašykite,  kiek  liko nepanaudota geltonų
  juostelių:rašykitespalvos  kodą ``G``,lygybės ženklą (``=``)ir juostelių
  skaičių; lygybės ženklas iš abiejų pusių turi būti atskirtas vienu tarpo
  simboliu.

- Trečioje eilutėje tokiu pačiu būdu įrašykite žalių juostelių likutį.

- Ketvirtoje eilutėje –raudonų juostelių likutį.

**Nurodymai**

- Sukurkite ir parašykite funkciją1, kuri suskaičiuotų, kiek
  buvosuklijuotavėliavėlių.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

**Duomenų ir rezultatų pavyzdžiai**

``U1.txt``

+---------+----------------------------+
| ::      | ::                         |
|         |                            |
|   5     |   Krūveliųskaičius         |
|   Z 14  |   Žalių juostelių          |
|   R 12  |   Raudonų juostelių        |
|   G 20  |   Geltonų juostelių        |
|   R 5   |   Raudonų juostelių        |
|   R 6   |   Raudonų juostelių        |
+---------+----------------------------+

``U1rez.txt``

+---------+----------------------------+
| ::      | ::                         |
|         |                            |
|   7     |   Vėliavėlių skaičius      |
|   G = 6 |   Liko geltonų juostelių   |
|   Z = 0 |   Liko žalių juostelių     |
|   R = 9 |   Liko raudonų juostelių   |
+---------+----------------------------+
