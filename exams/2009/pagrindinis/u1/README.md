Mainai
======

Dvi valstybės, *Gilija* ir *Eglija*, pagal mainų programą keičiasi dviem studentais. Kiekvienas iš jų išvykdamas gali pasiimti ne daugiau kaip 3000 vertės savo valstybės pinigų (gilai ir eglai) sumą, kurią nuvykęs iškeičia kitos valstybės valiuta. Šiose valstybėse cirkuliuoja tik metaliniai pinigai – įvairių nominalų monetos. Pinigų perkamoji galia vienoda, tačiau monetų nominalai skiriasi. Parašykite programą, kuri skaičiuotų, kiek kokių monetų gaus kiekvienas studentas ir kiekvieno studento iškeistų monetų kiekį. Keitimo sąlyga – mažiausias galimas skaičius monetų.

**Duomenys** pateikiami tekstiniame faile `U1.txt`. Pirmoje eilutė je nurodoma, kiek monetų nominalų yra *Gilijos* valstybėje, antroje – mažėjančiai (mažėjimo tvarka) išvardijami monetų nominalai, trečioje – mažėjančiai (mažėjimo tvarka) išvardijami *Gilijos* valstybės studento turimų nominalų monetų skaičiai. Nulis reiškia, kad to nominalo monetos studentas neturi. Kitose trijose eilutėse pateikiami analogiški duomenys apie *Eglijos* valstybės studento turimus pinigus. Monetų nominalų skaičius $n\ (1 \leq n \leq 50)$ kiekvienoje valstybėje gali būti skirtingas.

**Rezultatai** pateikiami tekstiniame faile `U1rez.txt`. Pirmiausia spausdinama, kiek kokių Eglijos valstybės monetų (nominalų mažėjimo tvarka) gaus *Gilijos* valstybės studentas išsikeitęs pinigus. Spausdinama po du skaičius eilutė je: monetos nominalas ir kiek to nominalo monetų gaus studentas. Jeigu studentas negaus nė vienos kurio nors nominalo monetos, tada spausdinamas nulis. Atskiroje eilutėje spausdinamas iškeistų monetų kiekis. Kitose eilutėse analogiškai spausdinami *Eglijos* valstybės studento pinigų keitimo rezultatai. Skaičiai skiriami vienu tarpu. 

**Pavyzdžiai**:

`U1.txt`

```
6
10 7 6 4 3 1
10 0 8 4 3 0
4
8 6 4 1
1 1 50 0
```

`U1rez.txt`

```
8 21
6 0
4 1
1 1
23
10 21
7 0
6 0
4 1
3 0
1 0
22
```

**Nurodymai**: 

- Programoje  būtinai naudokite vienmačius sveikųjų skaičių masyvus. 
- Programoje neturi būti sakinių, skirtų darbui su ekranu. 
- Parašykite funkciją, kuri skaičiuotų, kokią sumą pinigų keičia studentas. 