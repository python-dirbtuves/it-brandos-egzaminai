#!/usr/bin/env python3


def isvezioti_picas(f):
    # Nuskaitome įvesties failo pirmą eilutę, kurioje saugomas užsakovų skaičius
    # ir dienos kilometrų planas.
    uzsakovu_sk, km_planas = next(f).split()
    uzsakovu_sk, km_planas = int(uzsakovu_sk), int(km_planas)

    # Nustatomos pradinės kintamųjų reikšmės.
    atstumas = 0
    liko_uzsakovu = uzsakovu_sk

    # Šio ciklo pagalba vykdomas picų išvežiojimas skaičiuojant nuvažiuotą
    # atstumą ir likusių užsakovų skaičių.
    for liko_uzsakovu in reversed(range(uzsakovu_sk)):

        # Nuskaitomos sekančio užsakovo koordinatės.
        x, y = next(f).split()
        x, y = int(x), int(y)

        # Apskaičiuojamas nuvažiuotas atstumas.
        atstumas = atstumas + (abs(x) + abs(y)) * 2

        # Jei dienos kilometų planas viršytas, nutraukimas ciklas ir grąžinami
        # rezultatai.
        if atstumas > km_planas:
            break

    return liko_uzsakovu, atstumas


def programa():
    # Nuskaitomi įvesties duomenys
    with open('U1.txt') as f:
        liko_uzsakovu, atstumas = isvezioti_picas(f)

    # Įrašomi rezultatai
    with open('U1rez.txt', 'w') as f:
        print(liko_uzsakovu, atstumas, file=f)


if __name__ == '__main__':
    programa()
