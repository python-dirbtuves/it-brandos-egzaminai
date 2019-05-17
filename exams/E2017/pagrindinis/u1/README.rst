Šešioliktainiai skaičiai
========================

.. default-role:: math

Vincas turi tekstinį failą su piešinio duomenimis. Piešinys sudarytas iš
langelių. Šių langelių spalvas nusako trys sveikieji skaičiai nuo 0 iki 255
(RGB komponentės).

Vincui reikia paversti pradinius dešimtainius skaičius į šešioliktainį kodą ir
rezultatą įrašyti į tekstinį failą. Pavyzdžiui, geltonos spalvos langelio,
kurio RGB komponentės yra 255, 221 ir 0, spalvos šešioliktainis kodas bus
``FFDD00`` (dešimtainis skaičius 255 atitinka šešioliktainį ``FF``, 221
atitinka ``DD`` ir 0 atitinka ``00``).

Dešimtainis skaičius (nuo 0 iki 255) konvertuojamas į šešioliktainį skaičių
taip: šešioliktainio skaičiaus pirmasis skaitmuo yra **sveikoji dalis**,
dešimtainį skaičių dalijant iš 16, o antrasis šešioliktainio skaičiaus skaitmuo
yra dešimtainio skaičiaus dalybos iš 16 **liekana**. Šešioliktainiai skaitmenys
nuo 10 iki 15 koduojami atitinkamai raidėmis nuo ``A`` iki ``F``. Jei pirmasis
skaitmuo gaunamas nulis, jis irgi yra rašomas

**Parašykite programą**, kuri spalvų dešimtaines RGB komponentes įrašytų į
naują failą šešioliktainiais kodais.

**Pradiniai duomenys**

Duomenys pateikiami tekstiniame faile ``U1.txt``.

Duomenų faile įrašyta:

- pirmoje eilutėje – piešinio ilgis `a (1 \leq a \leq 10000)` ir plotis `b\ (1
  \leq b \leq 10000)`;

- kitose `a * b` eilutėse, einant per piešinio langelius iš kairės į dešinę ir
  iš viršaus į apačią, – po 3 skaičius, nusakančius langelio RGB komponentes.

**Rezultatai**

Rezultatus įrašykite tekstiniame faile ``U1rez.txt``.

Rezultatų failą sudaro `a` eilučių ir `b` stulpelių (atskirtų kabliataškiais).
Spalvų kodai įrašomi tokia pačia tvarka kaip ir pradiniame faile.

Kiekvienoje eilutėje turi būti `b` spalvų šešioliktainių kodų (sujungiami trys
šešioliktainiai dviženkliai skaičiai be tarpų), atskirtų kabliataškiais ``;``
(po paskutinio kodo kabliataškis nededamas).

**Nurodymai**

- Sukurkite funkciją, kuri grąžina dešimtainį skaičių, konvertuotą į
  šešioliktainį skaičių.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

- Programoje nenaudokite globalių pagalbinių kintamųjų.

**Duomenų ir rezultatų pavyzdžiai**

``U1.txt``::

  2 3
  0 128 0
  255 0 0
  255 255 255
  255 255 0
  255 0 0
  255 255 0

``U1rez.txt``::

  008000;FF0000;FFFFFF
  FFFF00;FF0000;FFFF00


Šaltinis
--------

http://nec.lt/failai/6996_IT-VBE-1_2017-GALUTINE.pdf
