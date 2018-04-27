Pirštinės
=========

Dėžėje yra skirtingo dydžio kairės ir dešinės rankos moteriškų ir vyriškų pirštinių.

**Parašykite programą**, kuri suskaičiuotų, kiek yra:

- vyriškų pirštinių porų;
- moteriškų pirštinių porų;
- atliekamų moteriškų pirštinių;
- atliekamų vyriškų pirštinių.

Porą sudaro to paties dydžio kairės ir dešinės rankų pirštinės ir, aišku, tik vyriškos arba tik moteriškos.

**Duomenys**

Duomenys yra tekstiniame faile `U1.txt`:

- Pirmoje eilutėje užrašytas pirštinių skaičius $n\ (1 \leq n \leq 100)$.
- Toliau atskirose eilutėse surašyti duomenys apie kiekvieną pirštinę:
    * pirmas skaičius 3 (vyriška) arba 4 (moteriška);
    * antras skaičius 1 (kairė s rankos) arba 2 (dešinė s rankos);
    * toliau sveikasis skaičius, reiškiantis pirštinės dydį.
    
**Rezultatai**

Tekstiniame faile `U1rez.txt` pateikite keturis skaičius:

- pirmoje eilutėje – kiek yra moteriškų pirštinių porų;
- antroje eilutėje – kiek yra vyriškų pirštinių porų;
- trečioje eilutėje – kiek yra atliekamų moteriškų pirštinių;
- ketvirtoje eilutėje – kiek yra atliekamų vyriškų pirštinių.

Jei vyriškų ir/arba moteriškų pirštinių porų nėra arba/ir neliko atliekamų vyriškų ir/arba moteriškų pirštinių, tai išveskite nulį (`0`).

**Nurodymai**

- Programoje naudokite sveikųjų skaičių masyvus.
- Parašykite procedūrą duomenims skaityti.
- Parašykite funkciją, kuri skaičiuotų, kiek yra vyriškų (moteriškų) pirštinių porų.
- Parašykite funkciją, kuri skaičiuotų, kiek liko atliekamų moteriškų (vyriškų) pirštinių.
- Programoje nenaudokite sakinių, skirtų darbui su ekranu. 

**Pavyzdys 1**

`U1.txt`

```
14
4 1 25
4 1 13
4 2 15
4 2 25
3 2 42
3 2 25
4 1 25
3 1 25
4 1 25
3 1 42
3 1 25
3 1 36
4 1 24
4 1 15
```

`U1rez.txt`

```
2
2
4
2
```

**Pavyzdys 2**

`U1.txt`

```
1
4 1 25
```

`U1rez.txt`

```
0
0
1
0
```