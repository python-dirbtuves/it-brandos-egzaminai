Krepšinis
=========

Krepšinio rungtynių metu sekretoriatas registruoja abiejų komandų kiekvieno krepšininko buvimo aikštelėje ir sėdėjimo ant atsarginių suolelio laikus minutėmis. 

Vienu metu aikštelėje žaidžia po 5 krepšininkus. 

Parašykite programą, kuri nustatytų vienos komandos: 

- startinį krepšininkų penketuką numerių didėjimo tvarka;
- krepš  ininko, kuris daugiausia laiko buvo aikštelėje, numerį ir laiką, o jeigu tokie buvo keli, tai nurodytų vieną, kurio numeris mažiausias;
- krepšininko, kuris daugiausia laiko sėdėjo ant atsarginių suolelio, numerį ir laiką, o jeigu tokie buvo keli, tai nurody tų vieną, kurio numeris
  mažiausias;

**Duomenys**

Vienos komandos duomenys yra tekstiniame faile `U1.txt`:

- Pirmoje eilutėje yra užrašytas krepšininkų skaičius $n\ (6 \leq n \leq 12)$.
- Toliau  atskirose  eilutėse  yra  surašyti  duomenys  apie  kiekvieną krepšininką  (sveikieji skaičiai):
    - pirmas skaičius eilutėje – krepšininko numeris $k\ (4 \leq k \leq 99)$;
    - antras skaičius eilutėje – laikų (žaista ir/arba ilsėtasi) skaičius $t\ (1 \leq t \leq 40)$;
    - toliau  eilutėje  surašyti  laikai:  teigiamas  skaičius – kiek  minučių būta  aikštelėje, neigiamas  skaičius – kiek  minučių  sėdėta  ant atsarginių  suolelio.  Pavyzdžiui: `18 –11 9 –2` reiškia, kad krepšininkas pirmas 18 min. žaidė, po to 11 min. sėdėjo ant atsarginių suolelio, vėl 9 min. žaidė ir likusias iki rungtynių pabaigos 2 min. sėdėjo.

*Pastaba.*  Rungtynių trukmė 40 min.

**Rezultatai**

Tekstiniame faile `U1Rez.txt` rezultatus pateikite tokia tvarka:

- pirmoje eilutėje – startinio penketuko krepšininkų numerius didėjančia seka;
- antroje eilutėje – krepšininko, kuris daugiausiai laiko buvo aikštelėje, numerį ir laiką. Jeigu tokie buvo keli, tai nurodykite vieną, kurio numeris mažiausias;
- trečioje eilutėje – krepšininko, kuris daugiausia laiko sėdėjo ant atsarginių suolelio, numerį ir laiką. Jeigu tokie buvo keli, tai nurodykite vieną, kurio numeris mažiausias.

Skaičius eilutėje skirkite vienu tarpo simboliu.

**Nurodymai**

- Programoje naudokite vienmačius masyvus.
- Parašykite funkciją duomenims į masyvus skaityti.
- Parašykite funkciją, kuri surastų masyve didžiausio elemento indeksą arba reikšmę.
- Programoje ne varto  kite sakinių, skirtų darbui su ekranu.

**Pavyzdys**

`U1.txt`

```
8
9 5 7 -5 13 -4 11
7 5 -3 12 -5 17 -3
25 7 12 -3 5 -5 7 -5 3
14 5 12 -3 10 -7 8
5 1 -40
33 5 15 -5 9 -3 8
11 5 -12 8 -5 12 -3
13 5 3 -4 25 -5 3
```

`U1rez.txt`

```
9 13 14 25 33
33 32
5 40
```

Šaltinis
--------

http://nec.lt/failai/2730_IT-1-2012.pdf