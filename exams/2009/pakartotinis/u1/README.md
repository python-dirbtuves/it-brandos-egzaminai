Turistai
========

*Gilijos* valstybės studentų grupė važiuoja susipažinti su *Eglijos* valstybės sostine. Kiekvienas grupės studentas išvykdamas gali pasiimti ne daugiau kaip 3000 vertės savo valstybės pinigų (gilų) sumą, kurią nuvykęs iškeičia kitos valstybės valiuta. Šiose valstybėse cirkuliuoja tik metaliniai pinigai – įvairių nominalų monetos. Pinigų perkamoji galia abiejose valstybėse vienoda. Studentai suskaičiavo, kad *Eglijos* pinigų (eglų) gaus daugiau, jeigu visos grupės turimus pinigus keis visus iš karto, o ne kiekvienas atskirai. Pinigai keičiami monetų nominalų mažė jimo tvarka.

**Parašykite programą**, kuri suskaičiuotų:

- kiek iš viso pinigų (gilų) turi studentų grupė;

- kiek kokių *Eglijos* valstybės monetų gaus studentai, iškeitę visos grupės pinigus;

- kiek iš viso studentai gaus *Eglijos* monetų;

- kiek liks nepakeistų pinigų.

**Duomenys** pateikiami tekstiniame faile `U1.txt`. Pirmoje eilutė je nurodomas *Gilijos* valstybės studentų skaičius $k\ (1 \leq k \leq 30)$, antroje – studentų turimos pinigų sumos, trečioje – *Eglijos* valstybės monetų nominalų skaičius $n\ (1 \leq n \leq 15)$, ketvirtoje – mažėjančiai (mažėjimo tvarka) išvardijami *Eglijos* valstybės monetų nominalai.

**Rezultatai** pateikiami tekstiniame faile `U1rez.txt`. Pirmoje eilutėje spausdinama, kiek iš viso studentų grupė turi pinigų (gilų). Toliau $n$ eilučių spausdinama po du skaičius eilutė je: *Eglijos* monetų nominalai (nominalų mažėjimo tvarka) ir kiek to nominalo monetų gaus studentų grupė. Skaičiai skiriami vienu tarpu. Jeigu studentai negaus nė vienos kurio nors nominalo monetos, tada spausdinamas nulis. Atskiroje eilutė je spausdinamas *Eglijos* valstybės monetų skaičius, kurį gaus studentų grupė. Paskutinėje eilutėje spausdinama, kiek studentams liks neiškeistų pinigų (gilų). Jeigu neiškeistų gilų neliks, spausdinamas nulis. 

**Pavyzdžiai**:

`U1.txt`

```
5
107 25 490 41 38
3
8 6 4
```

`U1rez.txt`

```
701
8 87
6 0
4 1
88
1
```

**Nurodymai**: 

- Programoje būtinai naudokite vienmačius sveikųjų skaičių masyvus.
- Studentų turimas pinigų sumas saugokite vienmačiame skaičių masyve.
- Parašykite funkciją, kuri skaičiuotų, kiek iš viso pinigų (gilų) turi *Gilijos* studentų grupė.
- Pinigai keičiami monetų nominalų mažėjimo tvarka: skaičiuokite, kiek daugiausia galima gauti didžiausio nominalo monetų, po to iš likusių pinigų apskaičiuokite, kiek daugiausia galima gauti antros pagal nominalo dydį monetų, po to trečios ir t. t.
- Programoje neturi būti sakinių, skirtų darbui su ekranu. 