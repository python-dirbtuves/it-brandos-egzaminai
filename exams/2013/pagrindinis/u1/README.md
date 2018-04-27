Siuntų tarnyba
==============

Siuntų tarnyba dirba mieste, kurio visos gatvės susikerta stačiais kampais, o kiekvienoje gatvėje sankryžos kartojasi lygiai kas 1 km. Siuntų tarnyba yra įsikūrusi prie centrinės sankryžos ir veža siuntinius įvairioms įmonėms, kurios yra įsikūrusios prie kitų šio miesto sankryžų.

Kad būtų patogiau, siuntų tarnybos vairuotojai įmonių adresus užrašo dviem sveikaisiais skaičiais – koordinatėmis $x$ ir $y$. Siuntų tarnybos adresas – koordinačių pradžios taškas $(0; 0)$.

Siuntų tarnybos vairuotojas pristato siuntinius iš eilės pagal gautą sąrašą. Nuvežęs kiekvieną siuntinį, vairuotojas grįžta į siuntų tarnybą.

Bendras nuvažiuotų kilometrų skaičius negali viršyti dienos kilometrų limito.

**Parašykite programą**, kuri nustatytų:

- kiek įmonių aptarnavo siuntų tarnyba;
- kiek iš viso nuvažiuota kilometrų;
- paskutinės aptarnautos įmonės pavadinimas.

**Duomenys**

Duomenys yra tekstiniame faile `U1.txt`:

- pirmoje eilutėje yra siuntų skaičius $n\ (1 \leq n \leq 50)$ ir dienos kilometrų limitas $m\ (21 \leq m \leq 500)$;
- kitose $n$ eilučių yra užsakymų sąrašas:
    * pirmose 10 pozicijų, pradedant pirmąja, yra įmonės pavadinimas;
    * vienas tarpo simbolis;
    * įmonės koordinatės $x$ ir $y$ $(–5 \leq x \leq 5, –5 \leq y \leq 5)$, atskirtos vienu tarpo simboliu.
    
**Rezultatai**

Tekstiniame faile `U1rez.txt` rezultatus įrašykite vienoje eilutėje tokia tvarka:

- kiek įmonių aptarnavo siuntų tarnyba ir vieno tarpo simbolis,
- kiek nuvažiavo kilometrų ir vieno tarpo simbolis,
- paskutinės aptarnautos įmonės pavadinimas.

**Nurodymai**

- Parašykite procedūrą duomenims skaityti.
- Parašykite funkciją, kuri apskaičiuotų kelionės atstumą kilometrais nuo siuntų tarnybos iki įmonės ir atgal.
- Parašykite procedūrą rezultatams išvesti.
- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

**Pavyzdys**

`U1.txt`

```
5 30
Siuntuva   2 3
Auda       3 –1
Kostisa    –3 –2
Linga      3 0
Austuva    –2 –4
```

`U1rez.txt`

```
3 28 Kostisa
```

Šaltinis
--------

http://nec.lt/failai/3679_2013-IT-1-uzd-intern.pdf