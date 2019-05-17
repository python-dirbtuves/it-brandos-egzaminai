Mokiniai
========

.. default-role:: math

Visi klasės mokiniai atliko testą kompiuteriu. Pirmiausia jie užrašė savo
vardą, o paskui atsakė į klausimus, pasirinkdami vieną iš keturių atsakymo
variantų (A, B, C, D).

Norėdamas įvertinti mokinius, tą patį testą atliko ir mokytojas. Jis į visus
klausimus atsakė teisingai.

**Parašykite programą**, kuri:

- nustatytų, į kelis klausimus kiekvienas mokinys atsakė teisingai;

- surikiuotų mokinius pagal teisingų atsakymų skaičių didėjimo tvarka (nuo
  mažiausio iki didžiausio), o jei šie skaičiai sutampa – pagal mokinio vardą
  abėcėlės tvarka.

**Pradiniai duomenys**

Duomenys yra tekstiniame faile ``U2.txt``:

- pirmoje eilutėje yra testą atlikusių asmenų skaičius `n\ (3 \leq n \leq 10)`,
  testo klausimų skaičius `m\ (4 \leq m \leq 10)`;

- antroje eilutėje – mokytojo testo sprendimo numeris;

- tolesnėse `n` eilučių yra šie duomenys, atskirti vienas nuo kito tarpo
  simboliais:

  * pirmose 10 pozicijų – testą atlikusio asmens vardas (pirmoji raidė –
    didžioji, visi vardai skirtingi);

  * testo atsakymai (eilutė iš `m` raidžių, be tarpų).

**Rezultatai**

Tekstiniame faile ``U2rez.txt`` rezultatus įrašykite tokia tvarka:

- pirmoje eilutėje – mokytojo vardą;

- kiekvienoje naujoje eilutėje – mokinių duomenis: vardą ir teisingų atsakymų
  skaičių, atskirtus vieno tarpo simboliu.

**Nurodymai**

Programoje naudokite struktūros duomenų tipą vieno asmens duomenims (vardui,
testo atsakymams ir teisingų atsakymų skaičiui) saugoti.  Programoje naudokite
masyvo duomenų tipą asmenų duomenims saugoti.  Sukurkite mokinių rikiavimo
funkciją 1 .  Sukurkite funkciją mokytojo ir mokinio atsakymams palyginti.
Sukurkite funkciją 1 duomenims skaityti ir funkciją 1 rezultatams spausdinti.
Programoje nenaudokite sakinių, skirtų darbui su ekranu.

**Duomenų ir rezultatų pavyzdys**

``U2.txt``::

  5 6
  3
  Simas BBBDDD
  Asta ABCDEA
  Juozapas ABCDEA
  Anupras ABCDEA
  Jonas ABCAAB

``U2rez.txt``::

  Juozapas
  Simas 2
  Jonas 3
  Anupras 6
  Asta 6


Šaltinis
--------

http://nec.lt/failai/5943_IT.zip
