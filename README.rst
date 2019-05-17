.. image:: https://travis-ci.org/python-dirbtuves/it-brandos-egzaminai.svg?branch=master
   :target: https://travis-ci.org/python-dirbtuves/it-brandos-egzaminai


Brandos egzaminų programavimo užduočių sprendimai
=================================================

Pilnus egzaminų užduočių aprašymus galima rasti `nec.lt <http://nec.lt/441/>`_
svetainėje.

Visos užduotys išspręstos naudojant Python_ programavimo kalbą.


Kaip paleisti sprendimų programas?
----------------------------------

Tam, kad paleisti sprendimų programas reikalinga **Python 3.6** ar vėlesnė
versija.

Visas sprendimų programas galite paleisti iš komandų eilutės::

  $ ./test

Tam, kad paleisti tam tikrų metų arba vieną konkretų testą, galite nurodyti
skriptui argumentą, kokius testus leisti, pavyzdžiui::

  $ ./test exams/2014

  $ ./test exams/2014/pagrindis

  $ ./test exams/2014/pagrindis/u1


Užduočių sprendimų struktūra
----------------------------

Kiekvienos egzamino užduoties kataloge rasite tokius failus:

``README.rst``
    Šiame faile pateikiama informacija apie užduotį ir nuorodą į užduoties
    dokumentą nec.lt svetainėje.

``uX.py``
    Šiame faile rasite užduoties programos sprendomo kodą.

``tests.py``
    Šiame faile yra automatiniai užduoties testai. Testų paskirtis įvykdyti
    programą, patikrinti ar ji grąžina teisingus rezultatus pagal pateiktus
    įvesties duomenis.


Visi failų pavadinimai sutampa su tais, kurių reikalauja egzamino užduotis, šis
failų ir jų pavadinimų sąrašas yra tik pavyzdinis.


Sprendimų sąrašas
=================


+----------+-----------------+----------------------------------------+-------+------------+
| Metai    | Egzaminas       | Užduotis                               | Balai | Sprendimas |
+==========+=================+========================================+=======+============+
| **2006** | |2006p|_        | |2006p1|_                              |       | |2006p1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2006p2|_                              |       |            |
+----------+-----------------+----------------------------------------+-------+------------+
| **2007** | |2007p|_        | |2007p1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2007p2|_                              |       |            |
+----------+-----------------+----------------------------------------+-------+------------+
| **2008** | |2008p|_        | |2008p1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2008p2|_                              |       |            |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2008k|_        | |2008k1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2008k2|_                              |       |            |
+----------+-----------------+----------------------------------------+-------+------------+
| **2009** | |2009p|_        | |2009p1|_                              |       | |2009p1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2009p2|_                              |       |            |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2009k|_        | |2009k1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2009k2|_                              |       |            |
+----------+-----------------+----------------------------------------+-------+------------+
| **2010** | |2010b|_        | |2010b1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2010b2|_                              |       |            |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2010p|_        | |2010p1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2010p2|_                              |       |            |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2010k|_        | |2010k1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2010k2|_                              |       |            |
+----------+-----------------+----------------------------------------+-------+------------+
| **2011** | |2011p|_        | |2011p1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2011p2|_                              |       |            |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2011k|_        | |2011k1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2011k2|_                              |       |            |
+----------+-----------------+----------------------------------------+-------+------------+
| **2012** | |2012p|_        | |2012p1|_                              |       | |2012p1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2012p2|_                              |       | |2012p2s|_ |
+----------+-----------------+----------------------------------------+-------+------------+
| **2013** | |2013z|_        | |2013z1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2013z2|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2013z3|_                              |       |            |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2013p|_        | |2013p1|_                              |       | |2013p1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2013p2|_                              |       | |2013p2s|_ |
+----------+-----------------+----------------------------------------+-------+------------+
| **2014** | |2014b|_        | |2014b1|_                              |       | |2014b1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2014b2|_                              |       | |2014b2s|_ |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2014p|_        | |2014p1|_                              |       | |2014p1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2014p2|_                              |       | |2014p2s|_ |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2014k|_        | |2014k1|_                              |       | |2014k1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2014k2|_                              |       | |2014k2s|_ |
+----------+-----------------+----------------------------------------+-------+------------+
| **2015** | |2015p|_        | |2015p1|_                              |       | |2015p1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2015p2|_                              |       |            |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2015k|_        | |2015k1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2015k2|_                              |       |            |
+----------+-----------------+----------------------------------------+-------+------------+
| **2016** | |2016p|_        | |2016p1|_                              |       | |2016p1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2016p2|_                              |       | |2016p2s|_ |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2016k|_        | |2016k1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2016k2|_                              |       |            |
+----------+-----------------+----------------------------------------+-------+------------+
| **2017** | |2017p|_        | |2017p1|_                              |       | |2017p1s|_ |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2017p2|_                              |       |            |
|          +-----------------+----------------------------------------+-------+------------+
|          | |2017k|_        | |2017k1|_                              |       |            |
|          |                 +----------------------------------------+-------+------------+
|          |                 | |2017k2|_                              |       |            |
+----------+-----------------+----------------------------------------+-------+------------+


.. |2006p| replace:: Pagrindinis
.. _2006p: http://nec.lt/failai/149_uzduotys_2006_VBE_IT.pdf
.. |2006p1| replace:: Elektros grandinės varžos skaičiavimas
.. _2006p1: exams/2006/pagrindinis/u1/README.rst
.. |2006p1s| replace:: sprendimas
.. _2006p1s: exams/2006/pagrindinis/u1/u1.py
.. |2006p2| replace:: Kelionė
.. _2006p2: exams/2006/pagrindinis/u2/README.rst

.. |2007p| replace:: Pagrindinis
.. _2007p: http://nec.lt/failai/80_uzduotys_2007_VBE_IT.pdf
.. |2007p1| replace:: Grybai
.. _2007p1: exams/2007/pagrindinis/u1/README.rst
.. |2007p2| replace:: Grybautojai
.. _2007p2: exams/2007/pagrindinis/u2/README.rst

.. |2008p| replace:: Pagrindinis
.. _2008p: http://nec.lt/failai/511_uzduotys_2008_VBE_IT.pdf
.. |2008p1| replace:: Tyrimas
.. _2008p1: exams/2008/pagrindinis/u1/README.rst
.. |2008p2| replace:: Transportas
.. _2008p2: exams/2008/pagrindinis/u2/README.rst

.. |2008k| replace:: Pakartotinis
.. _2008k: http://nec.lt/failai/870_2008_pakartotine_s_informacines_technologijos.zip
.. |2008k1| replace:: Metro
.. _2008k1: exams/2008/pakartotinis/u1/README.rst
.. |2008k2| replace:: Amžius
.. _2008k2: exams/2008/pakartotinis/u2/README.rst

.. |2009p| replace:: Pagrindinis
.. _2009p: http://nec.lt/failai/1044_uzduotys_2009_VBE_inf_technol.pdf
.. |2009p1| replace:: Mainai
.. _2009p1: exams/2009/pagrindinis/u1/README.rst
.. |2009p1s| replace:: sprendimas
.. _2009p1s: exams/2009/pagrindinis/u1/u1.py
.. |2009p2| replace:: Varžybos
.. _2009p2: exams/2009/pagrindinis/u2/README.rst

.. |2009k| replace:: Pakartotinis
.. _2009k: http://nec.lt/failai/1423_IT-2VBE-2009.pdf
.. |2009k1| replace:: Turistai
.. _2009k1: exams/2009/pakartotinis/u1/README.rst
.. |2009k2| replace:: Varžybos
.. _2009k2: exams/2009/pakartotinis/u2/README.rst

.. |2010b| replace:: Bandomasis
.. _2010b: http://nec.lt/failai/1506_IT_VBE_band_2010.pdf
.. |2010b1| replace:: Žirniai
.. _2010b1: exams/2010/bandomasis/u1/README.rst
.. |2010b2| replace:: Pasirinkimas
.. _2010b2: exams/2010/bandomasis/u2/README.rst

.. |2010p| replace:: Pagrindinis
.. _2010p: http://nec.lt/failai/1602_IT-pagr-2010.pdf
.. |2010p1| replace:: Šachmatų turnyras
.. _2010p1: exams/2010/pagrindinis/u1/README.rst
.. |2010p2| replace:: Gimtadienis
.. _2010p2: exams/2010/pagrindinis/u2/README.rst

.. |2010k| replace:: Pakartotinis
.. _2010k: http://nec.lt/failai/1904_IT-2-2010_uzduotis.pdf
.. |2010k1| replace:: Šachmatų turnyras
.. _2010k1: exams/2010/pakartotinis/u1/README.rst
.. |2010k2| replace:: Gimtadienis
.. _2010k2: exams/2010/pakartotinis/u2/README.rst

.. |2011p| replace:: Pagrindinis
.. _2011p: http://nec.lt/failai/2062_IT-VBE-1_2011.pdf
.. |2011p1| replace:: Pirštinės
.. _2011p1: exams/2011/pagrindinis/u1/README.rst
.. |2011p2| replace:: Šokiai
.. _2011p2: exams/2011/pagrindinis/u2/README.rst

.. |2011k| replace:: Pakartotinis
.. _2011k: http://nec.lt/failai/2425_IT-2-2011.pdf
.. |2011k1| replace:: Pirštinės
.. _2011k1: exams/2011/pakartotinis/u1/README.rst
.. |2011k2| replace:: Šokiai
.. _2011k2: exams/2011/pakartotinis/u2/README.rst

.. |2012p| replace:: Pagrindinis
.. _2012p: http://nec.lt/failai/2730_IT-1-2012.pdf
.. |2012p1| replace:: Krepšinis
.. _2012p1: exams/2012/pagrindinis/u1/README.rst
.. |2012p1s| replace:: sprendimas
.. _2012p1s: exams/2012/pagrindinis/u1/u1.py
.. |2012p2| replace:: Kauliukai
.. _2012p2: exams/2012/pagrindinis/u2/README.rst
.. |2012p2s| replace:: sprendimas
.. _2012p2s: exams/2012/pagrindinis/u2/u2.py

.. |2013z| replace:: Pavyzdinis
.. _2013z: http://nec.lt/failai/3398_2013-IT-pavyz-uzd.pdf
.. |2013z1| replace:: Skaičių dalumas
.. _2013z1: exams/2013/pavyzdinis/u1/README.rst
.. |2013z2| replace:: Batai
.. _2013z2: exams/2013/pavyzdinis/u2/README.rst
.. |2013z3| replace:: Žvejai
.. _2013z3: exams/2013/pavyzdinis/u3/README.rst

.. |2013p| replace:: Pagrindinis
.. _2013p: http://nec.lt/failai/3679_2013-IT-1-uzd-intern.pdf
.. |2013p1| replace:: Siuntų tarnyba
.. _2013p1: exams/2013/pakartotinis/u1/README.rst
.. |2013p1s| replace:: sprendimas
.. _2013p1s: exams/2013/pagrindinis/u1/u1.py
.. |2013p2| replace:: Miestai ir apskritys
.. _2013p2: exams/2013/pakartotinis/u2/README.rst
.. |2013p2s| replace:: sprendimas
.. _2013p2s: exams/2013/pagrindinis/u2/u2.py

.. |2014b| replace:: Bandomasis
.. _2014b: http://nec.lt/failai/4118_2014-IT-bandomasis.pdf
.. |2014b1| replace:: Picerija
.. _2014b1: exams/2014/bandomasis/u1/README.rst
.. |2014b1s| replace:: sprendimas
.. _2014b1s: exams/2014/bandomasis/u1/u1.py
.. |2014b2| replace:: Savivaldybės ir apskritys
.. _2014b2: exams/2014/bandomasis/u2/README.rst
.. |2014b2s| replace:: sprendimas
.. _2014b2s: exams/2014/bandomasis/u2/u2.py

.. |2014p| replace:: Pagrindinis
.. _2014p: http://nec.lt/failai/4429_2014-IT-VBE.pdf
.. |2014p1| replace:: Balsavimo rezultatai
.. _2014p1: exams/2014/pagrindinis/u1/README.rst
.. |2014p1s| replace:: sprendimas
.. _2014p1s: exams/2014/pagrindinis/u1/u1.py
.. |2014p2| replace:: Marsaeigis
.. _2014p2: exams/2014/pagrindinis/u2/README.rst
.. |2014p2s| replace:: sprendimas
.. _2014p2s: exams/2014/pagrindinis/u2/u2.py

.. |2014k| replace:: Pakartotinis
.. _2014k: http://nec.lt/failai/4914_2014-IT-1_uzd-PK.pdf
.. |2014k1| replace:: Balsavimo rezultatai
.. _2014k1: exams/2014/pakartotinis/u1/README.rst
.. |2014k1s| replace:: sprendimas
.. _2014k1s: exams/2014/pakartotinis/u1/u1.py
.. |2014k2| replace:: Marsaeigis
.. _2014k2: exams/2014/pakartotinis/u2/README.rst
.. |2014k2s| replace:: sprendimas
.. _2014k2s: exams/2014/pakartotinis/u2/u2.py

.. |2015p| replace:: Pagrindinis
.. _2015p: http://www.nec.lt/failai/5256_IT-VBE-1_2015.pdf
.. |2015p1| replace:: Dalybos
.. _2015p1: exams/2015/pagrindinis/u1/README.rst
.. |2015p1s| replace:: sprendimas
.. _2015p1s: exams/2015/pagrindinis/u1/u1.py
.. |2015p2| replace:: Avys
.. _2015p2: exams/2015/pagrindinis/u2/README.rst

.. |2015k| replace:: Pakartotinis
.. _2015k: http://nec.lt/failai/5943_IT.zip
.. |2015k1| replace:: Lobis
.. _2015k1: exams/2015/pakartotinis/u1/README.rst
.. |2015k2| replace:: Mokiniai
.. _2015k2: exams/2015/pakartotinis/u2/README.rst

.. |2016p| replace:: Pagrindinis
.. _2016p: http://nec.lt/failai/6287_IT-VBE-1_2016-GALUTINIS.pdf
.. |2016p1| replace:: Kuprinės
.. _2016p1: exams/2016/pagrindinis/u1/README.rst
.. |2016p1s| replace:: sprendimas
.. _2016p1s: exams/2016/pagrindinis/u1/u1.py
.. |2016p2| replace:: Mankšta
.. _2016p2: exams/2016/pagrindinis/u2/README.rst
.. |2016p2s| replace:: sprendimas
.. _2016p2s: exams/2016/pagrindinis/u2/u2.py

.. |2016k| replace:: Pakartotinis
.. _2016k: http://nec.lt/failai/6688_IT-VBE-2_2016.pdf
.. |2016k1| replace:: Ūgis
.. _2016k1: exams/2016/pakartotinis/u1/README.rst
.. |2016k2| replace:: Takai
.. _2016k2: exams/2016/pakartotinis/u2/README.rst

.. |2017p| replace:: Pagrindinis
.. _2017p: http://nec.lt/failai/6996_IT-VBE-1_2017-GALUTINE.pdf
.. |2017p1| replace:: Šešioliktainiai skaičiai
.. _2017p1: exams/2017/pagrindinis/u1/README.rst
.. |2017p2| replace:: Piešinys
.. _2017p2: exams/2017/pagrindinis/u2/README.rst

.. |2017k| replace:: Pakartotinis
.. _2017k: http://nec.lt/failai/7333_IT-VBE-2_2017.pdf
.. |2017k1| replace:: Dešimtainiai skaičiai
.. _2017k1: exams/2017/pakartotinis/u1/README.rst
.. |2017p1s| replace:: sprendimas
.. _2017p1s: exams/2017/pagrindinis/u1/u1.py
.. |2017k2| replace:: Kvadratai
.. _2017k2: exams/2017/pakartotinis/u2/README.rst

.. _Python: https://www.python.org/
