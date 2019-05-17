Savivaldybės ir apskritys
=========================

.. default-role:: math

Lietuvoje yra 60 savivaldybių, priskiriamų dešimčiai apskričių. Įvairiuose
Švietimo ir mokslo ministerijos projektuose gali dalyvauti įvairių savivaldybių
mokyklos.

**Parašykite programą**, kuri suskaičiuoja:

- kiek apskrityje yra tokių savivaldybių,

- kiek daugiausia dalyvauja vienos savivaldybės mokyklų.

**Pradiniai duomenys**

Duomenys yra tekstiniame faile ``U2.txt``:

- pirmoje eilutėje užrašytas savivaldybių, dalyvaujančių projektuose, skaičius
  `k\ (1 \leq k \leq 60)`,

- toliau atskirose eilutėse įrašyti duomenys apie kiekvieną savivaldybę:

  * pirmose 20 pozicijų įr ašytas savivaldybės pavadinimas (vienas žodis,
    vartojamos tik lotynų abėcėlės raidės), po to mokyklų, dalyvaujančių
    projektuose, skaičius `n\ (1 \leq n \leq 100)`,

  * kitoje eilutėje pirmose 13 pozicijų įrašytas apskrities pavadinimas (vienas
    žodis, vartojamos tik lotynų abėcėlės raidės), kurioje yra ta savivaldybė.
    
**Rezultatai**

Tekstiniame faile ``U2rez.txt`` įrašykite šiuos duomenis:

- pirmoje eilutėje – kiek projektuose dalyvauja apskričių,

- toliau atskirose eilutėse įrašykite duomenis apie kiekvieną projektuose
  dalyvaujančią apskritį:

  * pirmose 13 pozicijų apskrities pavadinimas (vartojamos tik lotynų abėcėlės
    raidės),

  * dalyvaujančių savivaldybių skaičius, po to vienas tarpo simbolis,

  * kiek daugiausia dalyvauja vienos savivaldybės mokyklų,

  * rezultatai turi būti išrikiuoti nustatyto mokyklų skaičiaus mažėjimo
    tvarka. Esant vienodam mokyklų skaičiui – abėcėlės tvarka pagal apskrities
    pavadinimą (apskričių pavadinimai rašomi tik lotyniškomis raidėmis).
    
**Nurodymai**

- Programoje naudokite įrašo duomenų tipą.

- Naudokite vienmačius masyvus įrašų duomenims saugoti.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

**Pavyzdys**

``U2.txt``::

  5
  Jieznas
  1
  Kauno
  Jonava
  4
  Kauno
  Kavarskas
  3
  Utenos
  Lazdijai
  1
  Alytaus
  Simnas
  1
  Alytaus

``U2rez.txt``::

  3
  Kauno         2 4
  Utenos        1 3
  Alytaus       2 1


Šaltinis
--------

http://www.nec.lt/failai/4118_2014-IT-bandomasis.pdf
