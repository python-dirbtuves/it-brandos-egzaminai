Grybai
======

Petras liepos mėnesį kiekvieną kartą grįžęs iš miško užrašo, kiek rado baravykų, raudonikių ir lepšių. Retkarčiais Petras eina į mišką tą pačią dieną kelis kartus. 

Parašykite programą, kuri:

1. skaičiuotų kiekvieną grybavimo dieną surinktų grybų skaičių pagal rūšis (baravykai, raudonikiai, lepšės); 

2. nustatytų dieną, kurią rasta daugiausia grybų ir kiek jų tą dieną rasta. 

**Pradiniai duomenys** surašyti į tekstinį failą `U1.txt`. Pirmoje eilutėje įrašytas grybavimo kartų skaičius $n\ (1 \leq n \leq 100)$. Tolesnėse eilutė e pateikti duomenys apie grybus. Viena eilutė skiriama vieno grybavimo karto laimikiui. Joje įrašyti keturi skaičiai: dienos numeris $d\ (1 \leq d \leq 31)$, surinktų baravykų, raudonikių ir lepšių skaičiai. Petras, surašydamas skaičius faile, nesilaikė dienų nuoseklumo. 

**Rezultatai** turi būti spausdinami į tekstinį failą `U1rez.txt`. Kiekvienai dienai skiriama po vieną eilutę. Dienos turi būti spausdinamos didėjan čia tvarka. Reikia spausdinti tik tas dienas, kuriomis buvo rastas bent vienas grybas. Pirmiausia pateikiamas dienos numeris, toliau – kiek per tą dieną buvo surinkta baravykų, raudonikių ir lepšių (jei kurios nors rūšies grybo nerasta, spausdinamas nulis). Paskutinėje eilutėje spausdinami du skaičiai: dienos, kurią surinkta daugiausia grybų, numeris ir visų tą dieną surinktų grybų skaičius. (Jeigu yra kelios tokios dienos, tai reikia spausdinti dieną, kurios numeris mažesnis.) 

**Nurodymai**: 

- Rašydami programą naudokite tik vienmačius sveikųjų skaičių masyvus. 
- Parašykite funkciją dienos, kurią surinkta daugiausia grybų, numeriui rasti. 
- Parašykite procedūrą surinktų grybų pagal dienas sąrašui spausdinti faile. 
- Programoje neturi būti sakinių, skirtų darbui su ekranu. 

**Pavyzdys**:

`U1.txt`

```
11
2 8 4 0
3 1 0 9
1 2 3 4
5 4 14 2
2 4 4 4
3 0 0 0
15 25 45 13
28 13 13 13
16 2  0  2
16 5  15 25
3  4  44 444
```

`U1rez.txt`

```
1 2 3 4
2 12 8 4
3 5 44 453
5 4 14 2
15 25 45 13
16 7 15 27
28 13 13 13
3 502
```