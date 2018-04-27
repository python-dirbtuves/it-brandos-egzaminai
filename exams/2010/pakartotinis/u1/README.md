Šachmatų turnyras
=================

Mokykloje organizuojamas šachmatų turnyras, tačiau trūksta šachmatų žaidimo komplektų. Paaiškėjo, kad dalis mokinių turi namuose po vieną šachmatų žaidimo komplektą, kuriuose trūksta kai kurių juodų figūrų (baltų figūrų netrūksta). Mokytojas pasiūlė iš mokinių turimų figūrų sukomplektuoti pilnus šachmatų komplektus.

**Parašykite programą**, kuri suskaičiuotų, kiek galima sudaryti pilnų šachmatų žaidimo komplektų iš mokinių atneštų figūrų.

Vienos spalvos figūrų komplektą sudaro 8 pėstininkai, 2 bokštai, 2 žirgai, 2 rikiai, 1 karalius ir 1 valdovė.

**Duomenys**

Tekstiniame faile `U1.txt` yra kelios eilutės su sveikaisiais skaičiais.

- Pirmoje eilutėje yra užrašytas mokinių skaičius $N\ (1 \leq N \leq 100)$.
- Toliau yra $N$ eilučių, kuriose surašyti kiekvieno mokinio trūkstamų juodų figūrų skaičiai. Kiekvieno mokinio figūrų sąrašui skiriama viena eilutė. Trūkstamų juodų figūrų skaičiai surašyti tokia tvarka: pėstininkai, bokštai, žirgai, rikiai, karaliai ir valdovės. Jeigu kurios nors figūros netrūksta, toje vietoje parašytas nulis.

Duomenų failo pavyzdyje parašyta, kad pirmam mokiniui trūksta 1 pėstininko, 1 bokšto, 1 žirgo, 1 rikio ir 1 karaliaus, o valdovę turi.

**Rezultatas**

Tekstiniame faile `U1rez.txt` pateikite, kiek šachmatų žaidimo komplektų galima sudaryti iš mokinių atneštų figūrų.

**Pavyzdžiai**

`U1.txt`

```
6 
1 1 1 1 1 0 
4 0 0 2 0 1 
8 0 0 0 0 0 
3 1 2 2 0 1 
1 2 1 0 0 0 
1 2 0 1 0 1
```

`U1rez.txt`

```
3
```

**Nurodymai**

- Programoje **būtinai** naudokite vienmačius sveikų jų skaičių masyvus.
- Parašykite funkciją, kuri suskaičiuotų, kiek šachmatų galima sudaryti iš mokinių atneštų juodų figūrų.
- Programoje nenaudokite sakinių, skirtų darbui su ekranu. 
