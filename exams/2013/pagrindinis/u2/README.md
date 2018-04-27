Miestai ir apskritys
====================

Pagal Lietuvos Statistikos departamento duomenis 2009 m. Lietuvoje buvo 103 miestai, priskirti dešimčiai apskričių. Įvairiuose Švietimo ir mokslo ministerijos projektuose gali dalyvauti įvairūs miestai.

**Parašykite programą**, kuri apskaičiuotų projektuose dalyvaujančių apskričių skaičių ir miestų statistiką kiekvienoje apskrityje:

- kiek miestuose yra gyventojų,
- mažiausio miesto gyventojų skaičių.

**Duomenys**

Duomenys yra tekstiniame faile `U2.txt`:

- pirmoje eilutėje užrašytas miestų, dalyvaujančių projekte, skaičius $k\ (1 \leq k \leq 103)$;
- toliau atskirose eilutėse įrašyti duomenys apie kiekvieną miestą:
    * pirmose 20 pozicijų įrašytas miesto pavadinimas,
    * tolesnėse 13 pozicijų įrašytas apskrities pavadinimas,
    * gyventojų skaičius $n\ (100 \leq n \leq 600000)$.
    
**Rezultatai**

Tekstiniame faile `U2rez.txt` įrašykite šiuos duomenis:

- pirmoje eilutėje – kiek projekte dalyvauja apskričių,
- toliau atskirose eilutėse įrašykite duomenis apie kiekvieną projektuose dalyvaujančią apskritį:
    * pirmose 13 pozicijų apskrities pavadinimas,
    * mažiausio miesto gyventojų skaičius, tarpo simbolis,
    * kiek iš viso apskrities miestuose yra gyventojų.
- rezultatai turi būti išrikiuoti mažiausių miestų gyventojų skaičiaus didė jimo tvarka. Esant vienodam gyventojų skaičiui – abėcėlės tvarka pagal apskrities pavadinimą.

**Nurodymai**

- Programoje naudokite du įrašo duomenų tipus: pradiniams duomenims apie miestus ir rezultato duomenims apie apskritis laikyti.
- Naudokite vienmačius masyvus įrašų duomenims saugoti.
- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

**Pavyzdys **

`U2.txt`

```
15
Vilnius             Vilniaus     541278
Dusetos             Utenos       4211
Alytus              Alytaus      69859
Druskininkai        Alytaus      16890
Ignalina            Utenos       6307
Kavarskas           Utenos       753
Lazdijai            Alytaus      5027
Simnas              Alytaus      1940
Trakai              Vilniaus     5504
Utena               Utenos       33086
Veisiejai           Alytaus      1673
Vievis              Vilniaus     5246
Lentvaris           Vilniaus     11832
Visaginas           Utenos       28438
Zarasai             Utenos       8001
```

`U2rez.txt`

```
3
Utenos       753 80796
Alytaus      1673 95389
Vilniaus     5246 563860
```


Šaltinis
--------

http://nec.lt/failai/3679_2013-IT-1-uzd-intern.pdf