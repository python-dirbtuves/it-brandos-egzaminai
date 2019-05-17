Piešinys
========

.. default-role:: math

Spalvotų stačiakampių rinkinys aprašomas nurodant jų spalvą ir koordinates.

Stačiakampiai koordinačių sistemoje gali vieni kitus dengti. Sukurkite galutinį
piešinį, gaunamą iš eilės dedant vieną stačiakampį ant kito (naujojo
stačiakampio spalva pakeičia ankstesnę).

Vaizdo dydis yra `100 \times 100` langelių (`x` ir `y` koordinatės kinta nuo 0
iki 99). Pradinis piešinys nuspalvintas baltai (RGB kodas – 255 255 255).

**Parašykite programą**, kuri nustatytų naujojo piešinio langelių spalvas.

*Pastaba*. RGB – spalvų maišymo sistema, kurioje naudojamos trys bazinės
spalvos: raudona (R), žalia (G) ir mėlyna (B).

**Pradiniai duomenys**

Duomenys pateikiami tekstiniame faile ``U2.txt``.

Pirmoje eilutėje esantis sveikasis skaičius `n\ (1 \leq n \leq 100)` nurodo,
kiek yra stačiakampių.

Tolesnėse `n` eilučių pateikiami stačiakampių duomenys:

- pirmi du skaičiai – viršutinio kairiojo kampo koordinatės `x`, `y\ (0 \leq x
  \leq 99, 0 \leq y \leq99)`;

- du skaičiai – stačiakampio plotis ir ilgis `dx, dy\ (1 \leq dx \leq 20, 1
  \leq dy \leq 20, x+dx \leq 100, y+dy \leq 100)`;

- trys skaičiai, nusakantys stačiakampio spalvos RGB komponentes.

**Rezultatai**

Rezultatus pateikite tekstiniame faile ``U2rez.txt``.

Į rezultatų failą įrašykite ne visą piešinį, o tik iki paskutinių nuspalvintų
stulpelių ir eilučių (atmeskite baltus stulpelius iš dešinės ir baltas eilutes
iš apačios).

Rezultatų faile turi būti įrašyta:

- pirmoje eilutėje – galutinio piešinio ilgis `a` (eilučių skaičius) ir plotis
  `b` (stulpelių skaičius);

- kitose `a \times b` eilučių, einant per piešinio langelius iš kairės į dešinę
  ir iš viršaus į apačią, – po 3 skaičius, nusakančius langelio RGB
  komponentes.

.. image:: iliustracija.png
   :alt: Piešinio pavyzdys
   :align: center

Nurodymai

- Sukurkite funkciją, kuri ant piešinio uždeda stačiakampį.

- Programoje naudokite struktūros duomenų tipą stačiakampių duomenims saugoti.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

- Programoje nenaudokite globalių pagalbinių kintamųjų.

**Duomenų ir rezultatų pavyzdys**

``U2.txt``::

  3
  0 0 2 2 0 128 0
  0 1 3 1 255 255 0
  1 0 1 2 255 0 0

``U2rez.txt``::

  2 3
  0 128 0
  255 0 0
  255 255 255
  255 255 0
  255 0 0
  255 255 0


Šaltinis
--------

http://nec.lt/failai/6996_IT-VBE-1_2017-GALUTINE.pdf
