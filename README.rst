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

.. list-table::
  :header-rows: 1

  * - Egzaminas
    - Užduočių sprendimai

  * - `2006. Pagrindinis <http://nec.lt/failai/149_uzduotys_2006_VBE_IT.pdf>`_
    - | 1 užduotis. Elektros grandinės varžos skaičiavimas
      | 2 užduotis. Kelionė

  * - `2007. Pagrindinis <http://nec.lt/failai/80_uzduotys_2007_VBE_IT.pdf>`_
    - | 1 užduotis. Grybai
      | 2 užduotis. Grybautojai

  * - `2008. Pagrindinis <http://nec.lt/failai/511_uzduotys_2008_VBE_IT.pdf>`_
    - | 1 užduotis. Tyrimai
      | 2 užduotis. Transportas

  * - `2008. Pakartotinis (zip)
      <http://nec.lt/failai/870_2008_pakartotine_s_informacines_technologijos.zip>`_
    - | 1 užduotis. Metro
      | 2 užduotis. Amžius

  * - `2009. Pagrindinis <http://nec.lt/failai/1044_uzduotys_2009_VBE_inf_technol.pdf>`_
    - | 1 užduotis. Mainai
      | 2 užduotis. Varžybos

  * - `2009. Pakartotinis <http://nec.lt/failai/1423_IT-2VBE-2009.pdf>`_
    - | 1 užduotis. Turistai
      | 2 užduotis. Varžybos (pakartotinis)

  * - `2010. Pagrindinis <http://nec.lt/failai/1602_IT-pagr-2010.pdf>`_
    - | 1 užduotis. Šachmatų turnyras
      | 2 užduotis. Gimtadienis

  * - `2010. Pakartotinis <http://nec.lt/failai/1904_IT-2-2010_uzduotis.pdf>`_
    - | 1 užduotis. Šachmatų turnyras (pakartotinis)
      | 2 užduotis. Gimtadienis (pakartotinis)

  * - `2010. Bandomasis <http://nec.lt/failai/1506_IT_VBE_band_2010.pdf>`_
    - | 1 užduotis. Žirniai
      | 2 užduotis. Pasirinkimas

  * - `2011. Pagrindinis <http://nec.lt/failai/2062_IT-VBE-1_2011.pdf>`_
    - | 1 užduotis. Pirštinės
      | 2 užduotis. Šokiai

  * - `2011. Pakartotinis <http://nec.lt/failai/2425_IT-2-2011.pdf>`_
    - | 1 užduotis. Pirštinės (pakartotinis)
      | 2 užduotis. Šokiai (pakartotinis)

  * - `2012. Pagrindinis <http://nec.lt/failai/2730_IT-1-2012.pdf>`_
    - | `1 užduotis. Krepšinis
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2012/pagrindinis/u1>`_
      | `2 užduotis. Kauliukai
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2012/pagrindinis/u2>`_

  * - `2013. Pagrindinis <http://nec.lt/failai/3679_2013-IT-1-uzd-intern.pdf>`_
    - | `1 užduotis. Siuntų tarnba
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2013/pagrindinis/u1>`_
      | `2 užduotis. Miestai ir apskritys
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2013/pagrindinis/u2>`_

  * - `2013. Pavyzdinės <http://nec.lt/failai/3398_2013-IT-pavyz-uzd.pdf>`_
    - | 1 užduotis. Skaičių dalumas
      | 2 užduotis. Batai
      | 3 užduotis. Žvejai

  * - `2014. Pagrindinis <http://nec.lt/failai/4429_2014-IT-VBE.pdf>`_
    - | `1 užduotis. Balsavimo rezultatai
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2014/pagrindinis/u1>`_
      | `2 užduotis. Marsaeigis
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2014/pagrindinis/u2>`_

  * - `2014. Pakartotinis <http://nec.lt/failai/4914_2014-IT-1_uzd-PK.pdf>`_
    - | `1 užduotis. Balsavimo rezultatai (pakartotinis)
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2014/pakartotinis/u1>`_
      | `2 užduotis. Marsaeigis (pakartotinis)
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2014/pakartotinis/u2>`_

  * - `2014. Bandomasis <http://nec.lt/failai/4118_2014-IT-bandomasis.pdf>`_
    - | `1 užduotis. Picerija
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2014/bandomasis/u1>`_
      | `2 užduotis. Savivaldybės ir apskritys
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2014/bandomasis/u2>`_

  * - `2015. Pagrindinis <http://www.nec.lt/failai/5256_IT-VBE-1_2015.pdf>`_
    - | 1 užduotis. Dalybos
      | 2 užduotis. Avys

  * - `2015. Pakartotinis (zip) <http://nec.lt/failai/5943_IT.zip>`_
    - | 1 užduotis. Lobis
      | 2 užduotis. Mokiniai

  * - `2016. Pagrindinis <http://nec.lt/failai/6287_IT-VBE-1_2016-GALUTINIS.pdf>`_
    - | `1 užduotis. Kuprinės
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2016/pagrindinis/u1>`_
      | `2 užduotis. Mankšta
        <https://github.com/python-dirbtuves/it-brandos-egzaminai/tree/master/exams/2016/pagrindinis/u2>`_

  * - `2016. Pakartotinis <http://nec.lt/failai/6688_IT-VBE-2_2016.pdf>`_
    - | 1 užduotis. Ūgis
      | 2 užduotis. Takai

  * - `2017. Pagrindinis <http://nec.lt/failai/6996_IT-VBE-1_2017-GALUTINE.pdf>`_
    - | 1 užduotis. Šešioliktainiai skaičiai
      | 2 užduotis. Piešinys

  * - `2017. Pakartotinis <http://nec.lt/failai/7333_IT-VBE-2_2017.pdf>`_
    - | 1 užduotis. Dešimtainiai skaičiai
      | 2 užduotis. Kvadratai


.. _Python: https://www.python.org/
