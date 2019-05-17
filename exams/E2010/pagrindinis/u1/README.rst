Šachmatų turnyras
=================

.. default-role:: math

Mokykloje organizuojamas šachmatų turnyras, tačiau trūksta šachmatų žaidimo
komplektų. Paaiškėjo, kad dalis mokinių turi namuose šachmatų žaidimo
komplektus, kuriuose trūksta kai kurių baltų figūrų (juodų figūrų netrūksta).
Jie turimus komplektus atnešė į mokyklą.

**Parašykite programą**, kuri suskaičiuotų, kiek pilnų šachmatų žaidimo
komplektų galima sudaryti iš mokinių atneštų figūrų.

Vienos spalvos figūrų komplektą sudaro 8 pėstininkai, 2 bokštai, 2 žirgai, 2
rikiai, 1 karalius ir 1 valdovė.

**Duomenys**

Tekstiniame faile ``U1.txt`` yra kelios eilutės su sveikaisiais skaičiais.

- Pirmoje eilutė je užrašytas mokinių skaičius `N\ (1 \leq N \leq 100)`.

- Toliau yra `N` eilučių, kuriose surašyti mokinių atneštų baltų figūrų
  skaičiai. Kiekvieno mokinio figūrų sąrašui skiriama viena eilutė. Kokių ir
  kiek mokinys atnešė baltų figūrų, surašyta tokia tvarka: pėstininkai,
  bokštai, žirgai, rikiai, karaliai ir valdovės. Jeigu kurios nors figūros
  mokinys neatnešė, toje vietoje parašytas nulis. Duomenų failo pavyzdyje
  parašyta, kad pirmas mokinys atnešė 22 pėstininkus, 3 bokštus, 5 žirgus, 6
  rikius ir 2 karalius, o valdovių neatnešė.

**Rezultatas**

Tekstiniame faile ``U1rez.txt`` pateikite, kiek šachmatų žaidimo komplektų
galima sudaryti iš mokinių atneštų figūrų.

**Pavyzdžiai**

``U1.txt``::

  4
  22 3 5 6 2 0
  1 1 1 1 1 1
  8 4 4 4 1 2
  5 3 3 3 0 2

``U1rez.txt``::

  4

**Nurodymai**

- Programoje būtinai naudokite vienmačius sveikųjų skaičių masyvus.

- Parašykite funkciją, kuri skaičiuotų, kiek šachmatų komplektų galima sudaryti
  iš mokinių atneštų baltų figūrų.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu. 
