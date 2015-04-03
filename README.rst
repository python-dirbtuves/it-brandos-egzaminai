Brandos egzaminų programavimo užduočių sprendimai
=================================================

Pilnus egzaminų užduočių aprašymus galima rasti `nec.lt <http://nec.lt/441/>`_
svetainėje.

Visos užduotys išspręstos naudojant Python_ programavimo kalbą.

Kodėl Python?
-------------

Lietuvoje brandos egzaminų programavimo užduotis leidžiama spręsti naudojant
Pascal arba C/C++ programavimo kalbas. Tačiau šios kalbos yra žemo lygio
programavimo kalbos, kurios nėra patogios mokytis programavimo. C/C++ yra sena
kalba, tačiau vis dar plačiai naudojamos ir šiandien, tuo tarpu Pascal yra
labai sena ir šiandien beveik nebenaudojama programavimo kalba.

C/C++ programavimo kalba dažniausiai naudojama tada, kai siekiama labai greito
veikimo, technologijos ir platformos neutralumo arba kai programa turi
glaudžiai bendrauti su kompiuterio ar mikrokontrolerių geležimi. Tačiau C/C++
būdama žemo lygio programavimo kalba reikalauja suprasti daug techninių
detalių, kurios apsunkina programavimo pagrindų mokymąsi. Studentai pasirinkę
programavimo kryptį tikrai turėtų susipažinti so C/C++ kalbomis, tačiau
mokiniams tai yra tikrai per daug.

Python yra šiuolaikiška, lengvai išmokstama, aukšto lygio programavimo kalba.
Python yra interpretuojama kalba, todėl programos nereikia kompiliuoti, taip
pat Python turi dinaminę tipų sistemą, kuri leidžia išvengti rūpesčių su
atminties valdymu ir leidžia daugiau gilintis į sprendžiamą užduotį, o ne į
žemo lygio mašinines problemas. Python yra universali programavimo kalba, todėl
ji yra taikoma įvairiausiose srityse, pradedant nuo mikrokontrolerių ar
akademinių taikymų, baigiant interneto svetainėmis ar darbastalio programomis.


Kaip paleisti sprendimų programas?
----------------------------------

Visas sprendimų programas galite paleisti naudodami ``runtests.py`` skriptą. Iš
komandinės eilutės šis skriptas paleidžiamas taip::

    $ python3 runtests.py

Tam, kad paleisti tam tikrų metų arba vieną konkretų testą, galite nurodyti
skriptui argumentą, kokius testus leisti, pavyzdžiui::

    $ python3 runtests.py 2014

    $ python3 runtests.py 2014/pagrindis

    $ python3 runtests.py 2014/pagrindis/u1


Užduočių sprendimų struktūra
----------------------------

Visi užduočių sprendimai suskirstyti į katalogus pagal metus, egzamino sesijas
ir užduotis. Užduotys pavadintos ``u1``, ``u2`` ir pan. pavadinimais. Egzaminų
sesijos pavadintos ``bandomasis``, ``pagrindis`` ir ``pakartotinis``.

Kiekvienos užduoties kataloge rasite tokius failus:

``u1.py``
    Šiame faile rasite užduoties programos kodą.

``U1.txt``
    Šiame ir panašaus pobūdžio failuose rasite užduoties įvesties duomenis.

``tests.py``
    Šiame faile yra automatiniai užduoties testai. Testų paskirtis įvykdyti
    programą, patikrinti ar jei grąžinta teisingus rezultatus pagal pateiktus
    įvesties duomenis.

``README.rst``
    Šiame faile pateikiama informacija apie užduotį, nuorodą į užduoties
    dokumentą.

Visi failų pavadinimai sutampa su tais, kurių reikalauja egzamino užduotis, šis
failų ir jų pavadinimų sąrašas yra tik pavyzdinis.


.. _Python: https://www.python.org/
