Picerija
========

Picerija dirba mieste, kurio visos gatvės susikerta stačiais kampais, o kiekvienoje gatvėje sankryžos kartojasi lygiai $k$ as 1 km. Picerija yra įsikūrusi prie centrinės sankryžos ir veža picas užsakovams, kurie taip pat yra įsikūrę prie kitų šio miesto sankryžų.

Kad būtų patogiau, picerijos vairuotojas užsakovų adresus užrašo dviem sveikaisiais skaičiais – koordinatėmis $x$ ir $y$. Picerijos adresas – koordinačių pradžios taškas $(0; 0)$.

Picerijos vairuotojas pristato picas iš eilės pagal gautą sąrašą. Nuvežęs kiekvieną užsakymą, vairuotojas grįžta į piceriją.

Vairuotojas aptarnauja dar vieną užsakovą, jei bendras iki tol nuvažiuotų kilometrų skaičius neviršija dienos kilometrų plano ir yra nepristatytų užsakymų, priešingu atveju baigia darbą.

Vairuotojas važiuoja tik gatvėmis. Paveiksle pavaizduotas vienas galimas kelias iki užsakovo.

**Parašykite programą**, kuri nustatytų:

- kiek liko neaptarnautų užsakovų,
- kiek iš viso nuvažiuota kilometrų.

**Pradiniai duomenys**

Duomenys yra tekstiniame faile `U1.txt`:

- pirmoje eilutėje yra užsakovų skaičius $n\ (1 \leq n \leq 50)$ ir dienos kilometrų planas $m\ (0 \leq m \leq 500)$,
- kitose $n$ eilučių yra užsakovų koordi natės $x$ ir $y\ (–5 \leq x \leq 5, –5 \leq y \leq 5)$, atskirtos vienu tarpo simboliu.

**Rezultatai**

Tekstiniame faile `U1rez.txt` rezultatus pateikite vienoje eilutėje tokia tvarka:

- kiek liko neaptarnautų užsakovų ir vienas tarpo simbolis,
- kiek vairuotojas nuvažiavo kilometrų.

**Nurodymai**

- Parašykite procedūrą duomenims skaityti.
- Parašykite funkciją, kuri apskaičiuotų kelionės atstumą kilometrais nuo picerijos iki užsakovo ir atgal.
- Parašykite procedūrą rezultatams išvesti.
- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

**Pavyzdys**

`U1.txt`

```
5 30
2 3
3 –1
-2 –4
–3 0
–2 4
```

`U1rez.txt`

```
1 36
```


Šaltinis
--------

http://www.nec.lt/failai/4118_2014-IT-bandomasis.pdf