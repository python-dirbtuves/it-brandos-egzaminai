Žirniai
=======

.. default-role:: math

Ūkininkas atvežė į turgų parduoti žirnių, supakuotų po vieną ir po du
kilogramus. Kiekvienas pirkėjas perka ne daugiau kaip 10 kg ir ne mažiau kaip 1
kg žirnių. Ūkininkas iš pradžių nori išparduoti didesnes žirnių pakuotes. Jeigu
pirkėjas perka daugiau kaip 1 kg žirnių, ūkininkas duoda pakuotes po 2 kg ir,
jeigu reikia, 1 kg pakuotę (pvz., jei pirkėjas perka 5 kg žirnių, pardavėjas
jam duoda dvi 2 kg pakuotes ir vieną 1 kg pakuotę). Kai baigiasi 2 kg pakuotės,
tada ūkininkas pardavinėja likusias 1 kg pakuotes.

**Parašykite programą**, kuri suskaičiuotų:

- kiek 1 kg ir kiek 2 kg žirnių pakuočių buvo parduota;

- keli pirkėjai nusipirko bent vieną žirnių pakuotę;

- kiek kilogramų žirnių nusipirko paskutinis pirkė jas, dar gavęs bent vieną
  žirnių pakuotę.

**Duomenys**

Tekstiniame faile ``Z1.txt`` yra kelios eilutės su sveikaisiais skaičiais:

- pirmoje eilutėje yra du skaičiai: `N_1\ (1 \leq N_1 \leq 100)` – 1 kg žirnių
  pakuočių skaičius, kur į atvežė ūkininkas ir `N_2\ (1 \leq N_2 \leq 100)` – 2
  kg žirnių pakuočių skaičius, kurį atvežė ūkininkas;

- antroje eilutėje užrašytas pirkėjų skaičius `N\ (1 \leq N \leq 100)`;

- toliau yra `N` eilučių, kuriose surašyti pirkėjų pageidavimai pirkti tam
  tikrą kiekį žirnių po vieną skaičių eilutėje.

**Rezultatai**

Rezultatus pateikite tekstiniame faile ``Z1rez.txt``, kuriame turi būti trys
eilutės:

- pirmoje eilutėje spausdinkite du skaičius, atskirtus vienu tarpu: kiek buvo
  nupirkta žirnių pakuočių po 1 kg ir kiek po 2 kg; jeigu kuri nors pakuotė
  nebuvo nupirkta, rašyti nulį;

- antroje eilutėje spausdinkite, keli pirkėjai nusipirko bent vieną žirnių
  pakuotę;

- trečioje eilutėje spausdinkite, kelis kilogramus žirnių nusipirko paskutinis
  pirkėjas, dar gavęs bent vieną žirnių pakuotę.

**Nurodymai**

- Pirkėjų pageidavimus saugokite vienmačiame sveikųjų skaičių masyve.

- Parašykite procedūrą, kuri suskaičiuotų, kiek pirkėjų nusipirko bent vieną
  žirnių pakuotę ir kiek kilogramų žirnių nusipirko paskutinis pirkėjas, dar
  gavęs bent vieną pakuotę.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu. 

**Pavyzdys 1**

``Z1.txt``::

  8 6
  4
  5
  1
  4
  3

``Z1rez.txt``::

  3 5
  4
  3

**Pavyzdys 2**

``Z1.txt``::

  5 5
  5
  5
  9
  4
  7
  1

``Z1rez.txt``::

  5 5
  3
  1
