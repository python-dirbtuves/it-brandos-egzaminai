Kelionė
=======

.. default-role:: math

Tarp Vilniaus ir Klaipėdos kursuojančiam autobusui reikia sudaryti grafiką.
Žinomi atstumai tarp stotelių, autobuso išvykimo iš Vilniaus laikas (valandos
ir minutės) ir vidutinis autobuso greitis. Autobusas į Klaipėdą atvyksta tą
pačią parą. 

Greitis, laikas ir atstumas yra susieti formule `v = \frac{s}{t}`; čia `v` –
vidutinis greitis, `s` – atstumas, `t` – laikas, sugaištamas nuvažiuoti tam
atstumui. 

**Parašykite programą autobuso atvykimo į stoteles laikui apskaičiuoti.**
Skaičiavimus atlikite vienos minutės tikslumu. Laikykite, kad autobusas
stotelėse nesugaišta laiko. Programa turi skaityti duomenis iš tekstinio
``Duom2.txt`` failo. Pirmoje failo eilutėje yra 4 skaičiai: maršruto stotelių
skaičius, autobuso vidutinis greitis, išvykimo iš Vilniaus valanda ir minutės.
Stotelių yra ne daugiau kaip 100. 

Tolesnėse eilutėse surašyti duomenys apie stoteles. Kiekvienoje eilutėje yra
stotelės pavadinimas, užrašytas nuo eilutės pradžios, ir atstumas nuo
ankstesnės stotelės. Greitis skaičiuojamas kilometrais per valandą, atstumai –
kilometrais. Pavadinimui skirtos pirmos 15 eilutės pozicijų. 

*Pavyzdžiui*, Elektrėnai nuo Vilniaus yra per 50,5 km, Žiežmariai nuo Elektrėnų
– per 20 km. 

Rezultatus programa turi įrašyti į ``Rez2.txt`` failą: kiekvienoje eilutėje
turi būti pateiktas stotelės pavadinimas, kuriam skiriamos pirmos 15 eilutės
pozicijų, ir autobuso atvykimo į stotelę laikas kaip nurodyta rezultatų failo
pavyzdyje (po valandų skaičiaus paliekamas vienas tarpas ir rašomas
sutrumpinimas ``val.``, vėl vienas tarpas, minučių skaičius ir dar po vieno
tarpo – sutrumpinimas ``min.``). 

**Pavyzdys**:

``Duom2.txt``::

  6 70 10 15
  Elektrėnai      50.5
  Žiežmariai      20
  Kaunas          22.35
  Raseiniai       80
  Kryžkalnis      20
  Klaipėda        100.8

``Rez2.txt``::

  Elektrėnai      10 val. 58 min.
  Žiežmariai      11 val. 15 min.
  Kaunas          11 val. 34 min.
  Raseiniai       12 val. 43 min.
  Kryžkalnis      13 val. 0 min.
  Klaipėda        14 val. 26 min.

**Privalomi reikalavimai**:

- Duomenis ir rezultatus saugoti masyve (masyvuose) su įrašo tipo elementais. 

- Sukurti ir panaudoti procedūrą duomenims skaityti į masyvą su įrašo tipo
  elementais. 

- Sukurti ir panaudoti procedūrą skaičiavimams. 

- Sukurti ir panaudoti procedūrą rezultatams įrašyti į failą. 

- Programoje panaudoti funkciją, skaičiuojančią laiką (minutėmis), per kurį
  autobusas nuvažiuoja nurodytą atstumą: 

  .. code-block:: python

    def laikas(atstumas: float, greitis: float) -> int:
        return int(atstumas / greitis * 60)

  čia ``atstumas`` – autobuso nuvažiuotas atstumas kilometrais, ``greitis`` –
  autobuso vidutinis greitis kilometrais per valandą. 
