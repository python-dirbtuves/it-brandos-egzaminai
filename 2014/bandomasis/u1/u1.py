#!/usr/bin/env python3


def isvezioti_picas(lines):
    # Nuskaitome įvesties failo pirmą eilutę, kurioje saugomas užsakovų skaičius
    # ir dienos kilometrų planas.
    uzsakovu_sk, km_planas = map(int, lines.pop(0).split())

    # Nustatomas pradinis atstumas, kuris yra lygus nuliui.
    atstumas = 0

    # Šio ciklo pagalba vykdomas picų išvežiojimas skaičiuojant nuvažiuotą
    # atstumą ir likusių užsakovų skaičių.
    for line in lines[:uzsakovu_sk]:

        # Nuskaitomos sekančio užsakovo koordinatės.
        x, y = map(int, line.split())

        # Apskaičiuojamas nuvažiuotas atstumas.
        atstumas += (abs(x) + abs(y)) * 2

        # Sumažiname likusių užsakovų sakičių
        uzsakovu_sk -= 1

        # Jei dienos kilometų planas viršytas, nutraukimas ciklas ir grąžinami
        # rezultatai.
        if atstumas > km_planas:
            break

    return uzsakovu_sk, atstumas


def programa():
    # Nuskaitomi įvesties duomenys
    with open('U1.txt') as f:
        uzsakovu_sk, atstumas = isvezioti_picas(f.read().splitlines())

    # Įrašomi rezultatai
    with open('U1rez.txt', 'w') as f:
        print(uzsakovu_sk, atstumas, file=f)


if __name__ == '__main__':
    programa()
