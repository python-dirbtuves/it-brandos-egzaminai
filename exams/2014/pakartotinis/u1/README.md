Balsavimo rezultatai
====================

Tris naujus žaidimus kurianti įmonė nusprendė sutaupyti atsisakydama vieno iš jų. Parengtos tokios balsavimo taisyklės:

1. Įmonės vadovas įvertina žaidimus ir atrenka blogiausią žaidimą.

2. Kiekvienas įmonės darbuotojas įvertina visus 3 žaidimus, skirdamas kiekvienam nuo 1 iki 3 balų (kuo geresnis žaidimas tuo daugiau balų). Gali kelis žaidimus įvertinti vienodai.

3. Nustatoma, kurį iš žaidimų darbuotojas vertina blogiausiai. Jei jis blogiausiai įvertina du arba tris žaidimus, tai blogiausias žaidimas nustatomas pagal įmonės vadovo vertinimą.

4. Atskirai suskaičiuojama, kiek kartų kiekvienas žaidimas buvo įvertintas blogiausiai.

5. Jei ankstesniame žingsnyje suskaičiuota vieno žaidimo suma didesnė už kitų dviejų, tai tas žaidimas laikomas blogiausiu, priešingu atveju blogiausiu žaidimu laikomas tas, kurį atrinko vadovas.

**Parašykite programą**, kuri nustatytų:

- kiek kartų kiekvienas žaidimas buvo įvertintas blogiausiai,
- įmonėje atrinkto blogiausio žaidimo numerį.

**Pradiniai duomenys**

Duomenys yra tekstiniame faile `U1.txt`:

- pirmoje eilutėje yra įmonės darbuotojų skaičius $k\ (1 \leq k \leq 10)$,
- kitose $k$ eilučių yra už pirmąjį, antrąjį ir trečiąjį žaidimą darbuotojų skirti balai (trys bet kurie sveikieji skaičiai nuo 1 iki 3),
- paskutinėje eilutėje yra numeris žaidimo, kurį direktorius atrinko blogiausiu.

**Rezultatai**

Tekstiniame faile `U1rez.txt` rezultatus įrašykite tokia tvarka:

- pirmoje eilutėje trys skaičiai – atitinkamai kiek kartų kiekvienas žaidimas buvo įvertintas blogiausiai (šių skaičių suma turi būti lygi darbuotojų skaičiui),
- antroje eilutėje – įmonėje atrinkto blogiausio žaidimo numeris.

**Nurodymai**

- Parašykite blogiausio žaidimo (vieno darbuotojo vertinimu) nustatymo procedūrą.
- Parašykite funkciją, nustatančią blogiausią žaidimą.
- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

**Duomenų ir rezultatų pavyzdys**

`U1.txt`

```
8
2 1 3
1 2 3
3 3 2
2 1 3
2 3 2
3 3 2
2 2 2
1 3 3
2
```

`U1rez.txt`

```
2 4 2
2
```


Šaltinis
--------

http://nec.lt/failai/4914_2014-IT-1_uzd-PK.pdf