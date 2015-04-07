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

Papildomai su Python galima mokytis įvairesnių programavimo paradigmų, tokių
kaip funkcinis programavimas, objektinis programavimas, asinchroninis
programavimas ir pan.


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
    programą, patikrinti ar ji grąžina teisingus rezultatus pagal pateiktus
    įvesties duomenis.

``README.rst``
    Šiame faile pateikiama informacija apie užduotį, nuorodą į užduoties
    dokumentą.

Visi failų pavadinimai sutampa su tais, kurių reikalauja egzamino užduotis, šis
failų ir jų pavadinimų sąrašas yra tik pavyzdinis.


Pastabos dėl egzaminų užduočių
------------------------------

Kadangi Pascal ir C/C++ yra žemo lygio programavimo kalbos, o Python yra aukšto
lygio programavimo kalba, tarp šių kalbų yra nemažai skirtumų. Šiame skyrelyje
pateikiamos pastabos dėl užduočių formuluotės, kurios nėra visiškai tinkamos
aukšto lygio kalboms.

Įrašo tipo duomenų tipas
~~~~~~~~~~~~~~~~~~~~~~~~

Įrašo tipas yra Pascal savoka, C/C++ kalboje analogiškas tipas vadinamas
„struktūra“. Tuo tarpu Python kalboje, tokio dalyko kaip „įrašo tipas“ arma
„struktūra“ nėra.

Artimiausias analogas tikriausiai būdų ``dict`` tipas arba klasės. Kai kuriais
atvejais galima naudoti net gi ``collections.namedtuple``. Kurį duomenų tipą
geriausia taikyti, priklauso užduoties. Saugiausias variantas tikriausiai būtų
klasės.

Apibrėžties sritys
~~~~~~~~~~~~~~~~~~

Dažnai užduotyse pateikiamos duomenų apibrėžties sritys, pavyzdžiui, nurodoma
kiek objektų reikia nuskaityti, kokia tam tikro kintamojo minimali ir maksimali
reikšmės.

Tai palengvina užduotį statiškai tipizuotose kalbose, tokiose kaip Pascal ar
C/C++, tačau Python veikia dinaminis atminties valdymas, todėl iš anksto
apibrėžti kintamųjų tipų nereikia ir tokios galimybės net gi nėra.

Iš esmės, pateiktą informaciją apie apibrėžimo sritis galima panaudoti nebent
įvesties duomenų tikrinimui. Pavyzdžiui:

.. code-block:: python

    assert 2 <= n <= 50

Dėl tos pačios statinio tipizavimo priežasties, įvesties duomenyse dažniausiai
pateikiamas sekančių įrašų skaičius ir sudaroma prielaida, kad programos
autorius visus duomenis nusiskaitys į atmintį. Tuo tarpu Python kalba turtinga
aukšto lygio abstrakcijomis darbui su duomenimis. Python kalba turi
iteratorius, kurie leidžia duomenis skaityti ir apdoroti srautu. Tai reiškia,
kad nebūtina visų duomenų nusiskaityti į atminį, galima juos skaityti po vieną
eilutę ir iš karto apdoroti.

Nurodymai parašyti funkcijas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Užduotyse pasitaiko tokių nurodymų, kaip parašyti funkciją didžiausiai ar
mažiausiai reikšmei surasti, surasti masyvo indeksą pagal reikšmę ir pan.

Python kalboje, tokio pobūdžio funkcijos dažnai būna įsiūtos į kalbą.
Pavyzdžiui surasti masyvo indeksą pagal reikšmę galima taip:

.. code-block:: python

    array.index(value)

Mažiausios ir didžiausios reikšmės paiškai taip pat yra funkcijos:

.. code-block:: python

    min(array), max(array)



.. _Python: https://www.python.org/
