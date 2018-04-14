"""

### 2016 metų brandos egzaminas, pagrindinė sesija

[Oficialus egzamino užduoties tekstas](http://nec.lt/failai/6287_IT-VBE-1_2016-GALUTINIS.pdf).

2 užduotis. Mankšta
===================

Vytautas nusprendė vieną vasaros mėnesį mankštintis, atlikdamas keletą
nesudėtingų pratimų. Kaskart pasimankštinęs jis užsirašydavo, kuriuos pratimus
ir kiek kartų atliko.

Parašykite programą, kuri nustatytų, kiek iš viso kartų per mėnesį Vytautas
atliko kiekvieną pratimą.

Pagrindiniai duomenys
---------------------

Duomenys pateikiami tekstiniame faile `U2.txt`.

Pirmoje eilutėje pateikiamas vienas sveikasis skaičius `n (1<=n<=100)`,
nurodantis, kiek Vytautas užsirašė duomenų eilučių.

Tolesnėse `n` eilučių pateikiami Vytauto užsirašyti duomenys:

- pratimo pavadinimas (20 simbolių) ir vienas tarpo simbolis;

- kiek kartų buvo atliktas šis pratimas.

Rezultatai
----------

Rezultatus pateikite tekstiniame faile `U2rez.txt`.

Atskirose eilutėse užrašykite šiuos kiekvieno pratimo duomenis:

- pratimo pavadinimą ir tarpo simbolį;

- kiek iš viso kartų per mėnesį buvo atliktas šis pratimas.

Rezultatus išrikiuokite atlikimo kartų mažėjimo tvarka (jei skaičiai sutampa -
pratimų pavadinimų abėcėlės tvarka).

Nurodymai
---------

- Programoje naudokite struktūros duomenų tipą Vytauto duomenims saugoti.

- Sukurkite rikiavimo [funkciją][1].

- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

[1]: "Pascal programavimo kalboje procedūra."

Duomenų ir rezultatų pavyzdžiai
-------------------------------

### Duomenų failo pavyzdys

    10
    prisitraukimai       10
    atsispaudimai        15
    atsilenkimai         12
    prisitraukimai       4
    atsilenkimai         15
    atsilenkimai         10
    prisitraukimai       12
    atsilenkimai         10
    atsispaudimai        2
    atsispaudimai        2

### Rezultatų failo pavyzdys

    atsilenkimai         47
    prisitraukimai       26
    atsispaudimai        19

Sprendimas
==========

"""

from collections import defaultdict
from pathlib import Path
from typing import List, Iterator, Dict, NamedTuple, Any


# Struktūros duomenų tipas Vytauto duomenims saugoti
class Exercise(NamedTuple):
    name: str
    reps: int


def read(path: Path) -> Iterator[Exercise]:
    """
    [Generatorius](https://docs.python.org/3/glossary.html#term-generator),
    kuris skaito duomenų failą.
    """
    with open(path) as f:
        # Skaičius `n`, nurodantis kiek iš viso pratimų Vytautas užsirašė.
        n = int(next(f))
        # Įsitikiname, kad `n` atitinka užduotyje nurodytą intervalą.
        assert 1 <= n <= 100
        # Skaitome kuprinių svorius `n` kartų.
        for i, line in zip(range(n), f):
            # Duomenis saugome struktūros tipo pavidalu.
            yield Exercise(line[:20], int(line[21:]))


def aggregate(data: Iterator[Exercise]) -> Dict[str, int]:
    """
    Skaičiuojame, kiek iš viso kartų buvo atliktas kiekvienas pratimas.
    """
    # Kuriame žodyną, kurio kiekvieno naujo elemento reikšmė bus 0.
    agg: Dict[str, int] = defaultdict(int)
    for exercise in data:
        # Sumuojame kiekvieno pratimo atlikimų skaičių.
        agg[exercise.name] += exercise.reps
    return agg


def sort(items: List[Any]) -> None:
    """
    Paprasčiausias [Bubble Sort](http://en.wikipedia.org/wiki/Bubble_sort)
    rūšiavimo algoritmas, rūšiuojantis atvirkštine tvarka.
    """
    # Iteruojame per visus elements.
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j] < items[j + 1]:
                # Sukeičiame rūšiavimo tvarkos neatitinkančius elementus.
                items[j], items[j + 1] = items[j + 1], items[j]


def main(path: Path) -> None:
    # Skaitome duomenų failą ir apskaičiuojame rezultatus.
    agg = aggregate(read(path / 'U2.txt'))
    # Paruošiame rezultatų masyvą rūšiavimui.
    result = [(reps, name) for name, reps in agg.items()]
    # Rūšiuojame rezultatus.
    sort(result)
    # Rašome rezultatus į išvesties failą.
    with open(path / 'U2rez.txt', 'w') as f:
        for reps, name in result:
            print('%-20s' % name, reps, file=f)


# Jei programa vykdoma tiesiogiai, iškviečiame programos paleidimo funkciją.
if __name__ == '__main__':
    main(Path())
