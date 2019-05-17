from collections import defaultdict
from itertools import islice
from pathlib import Path
from typing import List, Iterator, Dict, NamedTuple, Any


# Struktūros duomenų tipas Vytauto duomenims saugoti
class Exercise(NamedTuple):
    name: str
    reps: int


def read(lines: Iterator[str]) -> Iterator[Exercise]:
    # Skaičius `n`, nurodantis kiek iš viso pratimų Vytautas užsirašė.
    n = int(next(lines))

    # Įsitikiname, kad `n` atitinka užduotyje nurodytą intervalą.
    assert 1 <= n <= 100

    # Skaitome kuprinių svorius `n` kartų.
    for name, reps in map(str.split, islice(lines, n)):
        # Duomenis saugome struktūros tipo pavidalu.
        yield Exercise(name, int(reps))


def aggregate(data: Iterator[Exercise]) -> Dict[str, int]:
    """Skaičiuojame, kiek iš viso kartų buvo atliktas kiekvienas pratimas."""
    # Kuriame žodyną, kurio kiekvieno naujo elemento reikšmė bus 0.
    agg: Dict[str, int] = defaultdict(int)
    for name, reps in data:
        # Sumuojame kiekvieno pratimo atlikimų skaičių.
        agg[name] += reps
    return agg


def sort(items: List[Any]) -> None:
    """Paprasčiausias `Bubble Sort`_ rūšiavimo algoritmas, rūšiuojantis
    atvirkštine tvarka.

    .. _Bubble Sort: http://en.wikipedia.org/wiki/Bubble_sort
    """
    # Iteruojame per visus elements.
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j] < items[j + 1]:
                # Sukeičiame rūšiavimo tvarkos neatitinkančius elementus.
                items[j], items[j + 1] = items[j + 1], items[j]


def main(path: Path) -> None:
    # Skaitome duomenų failą ir apskaičiuojame rezultatus.
    with open(path / 'U2.txt') as f:
        agg = aggregate(read(f))
    # Paruošiame rezultatų masyvą rūšiavimui.
    result = [(reps, name) for name, reps in agg.items()]
    # Rūšiuojame rezultatus.
    sort(result)
    # Rašome rezultatus į išvesties failą.
    with open(path / 'U2rez.txt', 'w') as f:
        for reps, name in result:
            print('%-20s' % name, reps, file=f)
