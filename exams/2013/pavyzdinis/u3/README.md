Žvejai
======

Vasaros pradžioje susibūrė žvejų mėgėjų grupė. Kiekvienas dalyvis, grįžęs iš žvejybos, užrašo, kiek sugavo karosų, karpių ir kuojų.

**Parašykite programą**, kuri skaičiuotų, kiek kiekvienas žvejys per vasarą sugavo atskirai karosų, karpių bei kuojų ir kuris žvejys sugavo daugiausia žuvų ir kiek jų sugavo.

**Pradiniai duomenys** surašyti tekstiniame faile `U2.txt`. Pirmoje eilutėje įrašytas žvejų skaičius $n\ (1 \leq n \leq 100)$. Tolesnėse eilutėse pateikiami duomenys apie kiekvieno žvejo sugautas žuvis. Viena eilutė skiriama žvejo vardui (pirmos 10 eilutės pozicijų) ir jo žvejybos dienų skaičiui $d\ (1 \leq d \leq 30)$ nurodyti. Tolesnės $d$ eilučių skiriamos to žvejo kiekvienos dienos sugautoms žuvims nurodyti: viena eilutė – vienai dienai, kiekvienoje eilutėje yra po tris sveikuosius skaičius – karosų skaičius $a\ (0 \leq a \leq 300)$, karpių skaičius $b\ (0 \leq b \leq 300)$ ir kuojų skaičius $c\ (0 \leq c \leq 300)$. Po to ta pačia tvarka pateikiami kitų žvejų duomenys.

**Rezultatus** pateikite tekstiniame faile `U2rez.txt`. Čia kiekvienoje eilutėje nuo pradžios spausdinkite žvejo vardą, toliau atskirai spausdinkite jo sugautų per vasarą žuvų skaičius – karosų, karpių ir kuojų. Žvejo vardui skirkite 10 pirmų eilutė s pozicijų, spausdinkite nuo eilutės pradžios. Toliau spausdinkite žuvų skaičius (kiekvienam skaičiui skirkite po 5 pozicijas). Failo pabaigoje atskira eilute spausdinkite daugiausia žuvų sugavusio žvejo vardą ir jo visų sugautų per vasarą žuvų bendrą skaičių. Jeigu yra keli tokie žvejai, tada spausdinkite pirmesnį esantį `U2.txt` faile.

**Nurodymai**

- Duomenims ir rezultatams apdoroti naudokite įrašo tipo kintamuosius ir masyvus su įrašo tipo elementais.
- Parašykite procedūrą duomenims skaityti.
- Parašykite procedūrą rezultatams (kas, kokių ir kiek sugavo žuvų) spausdinti.
- Parašykite funkciją geriausiam žvejui (sugavusiam daugiausia žuvų) rasti.
- Programoje nenaudokite sakinių, skirtų darbui su ekranu. 

**Pavyzdys**

`U2.txt`

```
4
Petras    3
5 13 8
4 0 5
16 1 0
Algis     1
9 6 13
Jurgis    4
4 14 2
4 4 15
16 15 251
1 2 3
Rita      2
6 65 4
4 4 13
```

`U2rez.txt`

```
Petras       25   14   13
Algis         9    6   13
Jurgis       25   35  271
Rita         10   69   17
Jurgis      331
```


Šaltinis
--------

http://nec.lt/failai/3398_2013-IT-pavyz-uzd.pdf