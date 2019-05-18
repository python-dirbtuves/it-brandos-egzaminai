from itertools import islice


def seconds(v, m, s):
    # Ši funkcija verčia valandas, minutes ir sekundes į sekundes.
    return v * 3600 + m * 60 + s


def main(path):
    with open(path / 'U2.txt') as f:
        # Skaitome starto duomenis.
        startas = {}
        n = int(next(f))
        for eilute in islice(f, n):
            slidininkas = eilute[:20]
            laikas = map(int, eilute[20:].split())
            startas[slidininkas] = seconds(*laikas)

        # Skaitome finišo duomenis.
        finisas = {}
        m = int(next(f))
        for eilute in islice(f, m):
            slidininkas = eilute[:20]
            laikas = map(int, eilute[20:].split())
            # Įsimename per kiek laiko sekundėmis slidininkas pasiekė finišą.
            finisas[slidininkas] = seconds(*laikas) - startas[slidininkas]

    # Rašome rezultatus į išvesties failą.
    with open(path / 'U2rez.txt', 'w') as f:
        # Rūšiojame slidininkus pagal laiką ir vardus.
        for laikas, slidininas in sorted(x[::-1] for x in finisas.items()):
            # Sekundes verčiame į minutes ir sekundes.
            m, s = divmod(laikas, 60)
            print(f'{slidininas:<20}{m} {s}', file=f)
