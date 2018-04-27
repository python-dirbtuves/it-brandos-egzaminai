Elektros grandinės varžos skaičiavimas
======================================

Iš fizikos kurso žinome, kad lygiagrečiai sujungtų laidininkų bendra varža skaičiuojama pagal formulę $\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} + \ldots + \frac{1}{R_n}$; čia  $R$ – lygiagrečiai sujungtų laidininkų varža, $R_1, R_2, \ldots, R_n$ – atskirų laidininkų varžos. 

Nuosekliai sujungtų laidininkų bendra varža skaičiuojama pagal formulę $R = R_1 + R_2 + \ldots + R_n$; čia $R$ – nuosekliai sujungtų laidininkų bendra varža, $R_1, R_2, \ldots, R_n$ – atskirų laidininkų varžos. 

**Parašykite programą, kuri apskaičiuotų grandinės bendrą varžą**, kai grandinę sudaro viena ar daugiau nuosekliai sujungtų grandinės dalių; kiekviena grandinės  dalis sudaryta iš dviejų ar daugiau lygiagrečiai sujungtų žinomos varžos laidininkų. 

Programa turi skaityti duomenis iš tekstinio `Duom1.txt` failo. Pirmoje failo eilut ėje įrašytas nuosekliai sujungtų grandinės dalių skaičius (ne daugiau kaip 100). Po  to atskirose eilutėse surašyti grandinę sudarančių dalių duomenys: lygiagrečiai sujungtų laidininkų skaičius (ne daugiau kaip 50) ir jų varžų reikšmės. 

Rezultatą – apskaičiuotą **grandinės bendrą varžą** – programa turi  įrašyti į `Rez1.txt` failą dviejų ženklų po kablelio tikslumu. 

**Pavyzdys **:

`Duom1.txt`

```
3
2 15 41
4 1 2 3 4
3 22 11 24
```

`Rez1.txt`

```
17.08
```

![Elektros grandinės diagrama](diagrama.png)

Skaičiavimas: $L_1 = \frac{1}{R_1} + \frac{1}{R_1}$; $L_2 = \frac{1}{R_3} + \frac{1}{R_4} + \frac{1}{R_5} + \frac{1}{R_6}$; $L_3 = \frac{1}{R_7} + \frac{1}{R_8} + \frac{1}{R_9}$; $R = \frac{1}{L_1} + \frac{1}{L_2} + \frac{1}{L_3}$ – grandinės bendra varža.

Programą įrašykite įkietojo disko katalogą `C:\Egzaminas`, suteikdami failui vardą pagalšabloną `R01_1.pas` (raidė ir pirmieji du  skaitmenys (`01`) – jūsų darbo vietos žymė, atskiras skaitmuo (`1`) – praktinės užduoties eilės numeris). Kitaip įvardyti failai nebus vertinami.

Gavę savo darbo vietos žyme pažymėtą diskelį, nepamirškite į jį nukopijuoti programos failo. 