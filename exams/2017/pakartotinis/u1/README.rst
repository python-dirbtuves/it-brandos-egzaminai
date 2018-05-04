Dešimtainiai skaičiai
=====================

.. default-role:: math

Motiejus turi tekstinį failą su piešinio duomenimis. Piešinys sudarytas iš
langelių. Šių langelių spalvas nusako šešioliktainiai kodai, sudaryti iš trijų
šešioliktainių dviženklių skaičių nuo 00 iki FF (RGB komponenčių).

Motiejui reikia paversti šešioliktainius kodus į dešimtainius skaičius ir juos
įrašyti į tekstinį failą. Pavyzdžiui, geltonos spalvos langelio šešioliktainis
kodas yra ``FFDD00``, kuris atitinka `255`, `221` ir `0` RGB dešimtaines
komponentes.

Šešioliktainis skaičius (nuo ``00`` iki ``FF``) konvertuojamas į dešimtainį
skaičių taip: šešioliktainio skaičiaus pirmasis skaitmuo dauginamas iš 16 ir
pridedamas antrasi s skaitmuo. Šešioliktainiai skaitmenys nuo ``A`` iki ``F``
atitinka skaičius nuo 10 iki 15. Pavyzdžiui, šešioliktainis skaičius ``C8``
konvertuojamas taip: `12 \times 16 + 8 = 200` (``C`` atitinka skaičių 12).

**Parašykite programą**, kuri spalvų šešioliktainius kodus įrašytų į naują
failą dešimtainėmis RGB komponentėmis (vienas šešioliktainis kodas atitinka
tris dešimtainius skaičius).

**Pradiniai duomenys**

Duomenys pateikiami tekstiniame faile ``U1.txt``.

Duomenų faile įrašyta:

- p irmoje eilutėje – piešinio ilgis `a\ (1 \leq a \leq 100 00)` ir plotis
  `b\ (1 \leq b \leq 100 00)`;

- kitose `a \times b` eilutėse, einant per piešinio langelius iš kairės į
  dešinę ir iš viršaus į apačią, – po vieną šešioliktainį kodą (sujungtus tris
  dviženklius šešioliktainius skaičius).

**Rezultatai**

Rezultatus įrašykite tekstiniame faile ``U1rez.txt``.

Rezultatų failą sudaro `a` eilučių ir `b` stulpelių (atskirtų kabliataškiais).
Spalvų RGB komponentės įrašomos tokia pačia tvarka kaip ir pradiniame faile.

Kiekvienoje eilutėje turi būti:

- `b` spalvų RGB (po tris skaičius, atskirtus tarpais) dešimtainių kodų,
  atskirtų kabliataškiais ``;`` (po paskutinio kodo kabliataškis nededamas).

**Nurodymai**

- Sukurkite funkciją, kuri grąžina šešioliktainį dviženklį skaičių, konvertuotą
  į dešimtainį skaičių.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

- Programoje nenaudokite globalių pagalbinių kintamųjų. 

**Duomenų ir rezultatų pavyzdžiai**

``U1.txt``::

  2 3
  008000
  FF0000
  FFFFFF
  FFFF00
  FF0000
  FFFF00

``U1rez.txt``::

  0 128 0;255 0 0;255 255 255
  255 255 0;255 0 0;255 255 0


Šaltinis
--------

http://nec.lt/failai/7333_IT-VBE-2_2017.pdf
