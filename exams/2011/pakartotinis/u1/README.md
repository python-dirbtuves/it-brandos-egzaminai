Pirštinės
=========

Dėžėje yra skirtingo dydžio kairės ir dešinės rankos moteriškų ir vyriškų pirštinių.

**Parašykite programą**, kuri suskaičiuotų, kiek yra skirtingo dydžio vyriškų ir kiek moteriškų pirštinių porų. Porą sudaro tik vyriškos arba tik moteriškos to paties dydžio kairės ir dešinės rankų pirštinės.

**Duomenys**

Duomenys yra tekstiniame faile `U1.txt`:

- Pirmoje eilutėje užrašytas pirštinių skaičius $n\ (1 \leq n \leq 100)$.
- Toliau atskirose eilutėse surašyti duomenys apie kiekvieną pirštinę:
    * pirmas skaičius 3 (vyriška) arba 4 (moteriška);
    * antras skaičius 1 (kairė s rankos) arba 2 (dešinės rankos);
    * trečias sveikasis skaičius, reiškiantis pirštinės dydį (maksimalus galimas dydis 50).
    
**Rezultatai**

Tekstiniame faile `U1rez.txt` pateikite tiek eilučių, kiek yra skirtingo dydžio pirštinių porų (vyriškų ir moteriškų pirštinių pora gali būti to paties dydžio). Kiekvienoje eilutėje turi būti trys skaičiai:

- pirmas skaičius – pirštinių poros dydis;
- antras skaičius – kiek to dydžio yra moteriškų pirštinių porų;
- trečias skaičius – kiek to dydžio yra vyriškų pirštinių porų.

Jeigu nėra kurio nors dydžio moteriškų (vyriškų) porų, tada išveskite `0` (nulį). Rezultatus pateikite pirštinių dydžių didėjimo tvarka. Jeigu to dydžio porų (vyriškų ir moteriškų) nėra, tai rezultatuose jų nerodykite. Tarp skaičių eilutėje spausdinkite po vieną tarpo simbolį.

**Nurodymai**

- Programoje naudokite sveikųjų skaičių masyvus.
- Parašykite procedūrą duomenims skaityti.
- Parašykite procedūrą, kuri skaičiuotų, kiek yra vyriškų (moteriškų) pirštinių porų.
- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

**Pavyzdys**

`U1.txt`

```
8
4 1 25
4 1 13
4 2 15
4 2 25
3 2 25
4 1 25
3 1 25
4 1 15
```

`U1rez.txt`

```
15 1 0
25 1 1
```