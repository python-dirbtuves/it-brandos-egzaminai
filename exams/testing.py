from pathlib import Path
from typing import List


def write(path: Path, lines: List[str]) -> None:
    path.write_text('\n'.join(lines))


def read(path: Path) -> List[str]:
    return path.read_text().splitlines()
