from itertools import islice
from pathlib import Path
from typing import Iterator


def weights(lines: Iterator[str]) -> Iterator[int]:
        # Skaičius `x`, nurodantis kelių mokinių kuprinės buvo pasvertos.
        x = int(next(lines))

        # Įsitikiname, kad `x` atitinka užduotyje nurodytą intervalą.
        assert 0 < x <= 100

        # Skaitome kuprinių svorius `x` kartų.
        yield from map(int, islice(lines, x))


def main(path: Path) -> None:
    # Randame sunkiausios kuprinės svorį.
    with open(path / 'U1.txt') as f:
        max_weight = max(weights(f))

    # Randame kuprines, kurios yra du ir daugiau kartų lengvesnės už sunkiausią kuprinę.
    with open(path / 'U1.txt') as f:
        lightest_count = sum(1 for x in weights(f) if max_weight >= x + x)

    # Rašome rezultatus į išvesties failą.
    with open(path / 'U1rez.txt', 'w') as f:
        print(max_weight, lightest_count, file=f)
