from itertools import islice
from pathlib import Path
from typing import Dict


def seconds(v: int, m: int, s: int) -> int:
    # Ši funkcija verčia valandas, minutes ir sekundes į sekundes.
    return v * 3600 + m * 60 + s


def save_results(path: Path, pabaiga: Dict[str, int]) -> None:
    with path.open('w') as f:
        # Rūšiuojame slidininkus pagal laiką ir vardus.
        for laikas, slidininkas in sorted((v, k) for k, v in pabaiga.items()):
            # Sekundes verčiame į minutes ir sekundes.
            m, s = divmod(laikas, 60)
            print(f'{slidininkas:<20}{m} {s}', file=f)


def main(path: Path) -> None:
    startas: Dict[str, int] = {}
    pabaiga: Dict[str, int] = {}

    with open(path / 'U2.txt') as f:
        # Skaitome starto duomenis.
        n = int(next(f))
        for eilute in islice(f, n):
            slidininkas = eilute[:20]
            laikas = map(int, eilute[20:].split())
            startas[slidininkas] = seconds(*laikas)

        # Skaitome finišo duomenis.
        m = int(next(f))
        for eilute in islice(f, m):
            slidininkas = eilute[:20]
            laikas = map(int, eilute[20:].split())
            # Įsimename per kiek laiko sekundėmis slidininkas pasiekė finišą.
            pabaiga[slidininkas] = seconds(*laikas) - startas[slidininkas]

    save_results(path / 'U2rez.txt', pabaiga)
