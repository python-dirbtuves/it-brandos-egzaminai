.. default-role:: literal

Slidininkai
===========

Slidininkai 10 km rungtyje startuoja pagal atrankos etapo rezultatus.
Slidininkas startuoja tiek laiko vėliau už lyderį, kiek laiko nuo jo yra
atsilikęs.

Parašykite programą, kuri pateiktų slidininkų rezultatų sąrašą pagal trasoje
sugaištą laiką didėjančiai. Per vienodą laiką nušliuožę slidininkai turi būti
rašomi abėcėliškai pagal simbolių eilutę, kurioje yra slidininką
identifikuojanti informacija.

**Pradiniai duomenys**

Duomenys pateikiami tekstiniame faile `U2.txt`. Visi skaičiai yra sveikieji.

Duomenų faile įrašyta:

- Pirmoje eilutėje užrašytas startuojančių slidininkų skaičius `n (1 \leq n
  \leq 30)`:math:.

- Tolesnėse ``n`` eilučių atsitiktine tvarka surašyti slidininkų starto
  duomenys.  Kiekvieno slidininko duomenys užrašyti atskiroje eilutėje: pirmose
  20 pozicijų yra simbolių eilutė, kurioje pateikta slidininką identifikuojanti
  informacija; po to starto laikas: valanda, minutė ir sekundė, atskirtos vienu
  tarpo simboliu.

- Toliau užrašytas finišavusių slidininkų skaičius `m (1 \leq m \leq 30)`:math:.

- Tolesnėse ``m`` eilučių surašyti slidininkų finišo duomenys. Kiekvieno slidininko
  duomenys užrašyti atskiroje eilutėje: pirmose 20 pozicijų yra simbolių
  eilutė, kurioje pateikta slidininką identifikuojanti informacija; po to
  finišo laikas: valanda, minutė ir sekundė, atskirtos vienu tarpo simboliu.

**Rezultatai**

Rezultatus įrašykite tekstiniame faile `U2rez.txt`.

- Vienoje eilutėje užrašykite vieno slidininko duomenis: pirmose 20 pozicijų –
  simbolių eilutę, kurioje  pateikta  slidininką  identifikuojanti informacija,
  atskirta  vienu  tarpo  simboliu,  po  to slidininko rezultatas:  minutės  ir
  sekundės,  atskirtos  vienu  tarpo  simboliu. 10 km rungtyje maksimalus
  slidininko sugaištas laikas yra  ne  daugiau kaip valanda.Jeigu  slidininkas
  nepasiekė finišo(jo nėra finišavusiųjų sąraše), tai rezultatų sąraše jo
  neturi būti.

- Rezultatai turi būti surikiuoti pagal trasoje sugaištą laiką didėjančiai. Per
  vienodą laiką nušliuožę slidininkai  rašomi  abėcėliškai  pagal  simbolių
  eilutę,  kurioje  yra  slidininką  identifikuojanti informacija.

**Nurodymai**

- Sukurkite ir parašykite funkciją1, kuri surikiuoja rezultatus.

- Sukurkite ir parašykite funkciją, kuri spausdina rezultatus tekstiniame faile.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

**Duomenų ir rezultatų pavyzdžiai**

+---------------------------------+-------------------------------+
| Duomenų failo pavyzdys          | Rezultatų failo pavyzdys      |
+---------------------------------+-------------------------------+
| `U2.txt`                        | `U2rez.txt`                   |
+---------------------------------+-------------------------------+
| ::                              | ::                            |
|                                 |                               |
|   6                             |   Zigmas Nosis        20 6    |
|   Petras A. Petraitis 15 20 00  |   Jurgis Jurgutis     30 10   |
|   Jurgis Jurgutis     16 12 12  |   Petras A. Petraitis 30 10   |
|   Rimas Jonas         15 15 59  |   Rytis Uosis Ainis   32 50   |
|   Zigmas Nosis        16 23 9   |   Romas Senasis       50 20   |
|   Romas Senasis       15 15 15  |                               |
|   Rytis Uosis Ainis   16 23 9   |                               |
|   5                             |                               |
|   Zigmas Nosis        16 43 15  |                               |
|   Petras A. Petraitis 15 50 10  |                               |
|   Romas Senasis       16 5 35   |                               |
|   Rytis Uosis Ainis   16 55 59  |                               |
|   Jurgis Jurgutis     16 42 22  |                               |
|                                 |                               |
+---------------------------------+-------------------------------+
