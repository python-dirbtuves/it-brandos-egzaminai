"""

### 2016 metų brandos egzaminas, pagrindinė sesija

[Oficialus egzamino užduoties tekstas](http://nec.lt/failai/6287_IT-VBE-1_2016-GALUTINIS.pdf).

1 užduotis. Kuprinės
====================

Atlikdami projektinį darbą, mokiniai pasvėrė visų mokyklos mokinių kuprines.

Parašykite programą, kuri apskaičiuoja, kelių mokinių kuprinės yra du ir daugiau
kartų lengvesnės už sunkiausią kuprinę.

Atlikdami šią užduotį, nenaudokite masyvų ar kitų duomenų struktūrų.

Pagrindiniai duomenys
---------------------

Duomenys pateikiami tekstiniame faile `U1.txt`.

Pirmoje eilutėje  yra įrašytas skaičius `x (1<=x<=100)`, nurodantis,  kelių
mokinių kuprinės buvo pasvertos.

Kitose eilutėse yra įrašyta po vieną skaičių, nurodantį kuprinių masę gramais.

Rezultatai
----------

Rezultatus pateikite tekstiniame faile `U1rez.txt`.

Užrašykite du skaičius, atskirtus tarpo simboliu:

- sunkiausios kuprinės masę gramais,

- kelios kuprinės yra du ir daugiau kartų už ją lengvesnės.

Nurodymai
---------

- Spręsdami šį uždavinį, nenaudokite dalybos veiksmo.

- Parašykite [funkciją][1], kuri randa sunkiausios kuprinės masę.

- Parašykite [funkciją][1], kuri apskaičiuoja, kelios kuprinės yra du ir
  daugiau kartų lengvesnės už sunkiausią kuprinę.

- Programoje nenaudokite masyvų ar kitų duomenų struktūrų.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu

[1]: "Pascal programavimo kalboje procedūra."

Duomenų ir rezultatų pavyzdžiai
-------------------------------

### A pvz.

#### Pradiniai duomenys

    6
    5000
    4500
    5500
    3500
    10000
    5650

#### Rezultatas

    10000 3

### B pvz.

#### Pradiniai duomenys

    3
    3000
    3500
    2000

#### Rezultatas

    3500 0

Sprendimas
==========

"""


def weights():
    """
    [Generatorius](https://docs.python.org/3/glossary.html#term-generator),
    kuris skaito kuprinių svorių failą.
    """
    with open('U1.txt') as f:
        # Skaičius `x`, nurodantis kelių mokinių kuprinės buvo pasvertos.
        x = int(next(f))
        # Įsitikiname, kad `x` atitinka užduotyje nurodytą intervalą.
        assert 1 <= x <= 100

        # Skaitome kuprinių svorius `x` kartų.
        for i in range(x):
            # Kadangi užduotis draudžia naudoti masyvus ir kitas duomenų
            # struktūras, nuskaitytus duomenis grąžiname tiesiogiai.
            yield int(next(f))


def main():
    # Randame sunkiausios kuprinės svorį.
    max_weight = max(weights())
    # Randame kuprines, kurios yra du ir daugiau kartų lengvesnės už sunkiausią
    # kuprinę.
    lightest_count = sum(1 for x in weights() if max_weight >= x + x)

    # Rašome rezultatus į išvesties failą.
    with open('U1rez.txt', 'w') as f:
        print(max_weight, lightest_count, file=f)


# Jei programa vykdoma tiesiogiai, iškviečiame programos paleidimo funkciją.
if __name__ == '__main__':
    main()
