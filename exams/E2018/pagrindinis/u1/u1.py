from collections import Counter


def main(path):
    with open(path / 'U1.txt') as f:
        # n - krūvelių skaičius.
        n = int(next(f))

        # Skaičiuojam kiek viso yra kiekvienos spalvos juostelių. Šiam tikslui panaudojame
        # „sumatorių“ `Counter`. `Counter` dėka išvengiama juostelių spalvų pradinių
        # reikšmių inicializavimo žingsnį.
        kruveles = Counter()
        for i in range(n):
            # Skaitom `n` krūvelių:
            # `s` - krūvelės spalva,
            # `k` - juostelių skaičius krūvelėje.
            s, k = next(f).split()
            kruveles[s] += int(k)

    # Vienai vėliavėlei reikia dviejų, kiekvienos juostelės spalvų.  Randame mažiausios
    # krūvelės juostelių skaičių ir daliname iš dviejų, dalinant naudojame *floor
    # division* operatorių, kuris grąžina tik sveikąją dalį.
    veleveliu = min(kruveles.values()) // 2

    with open(path / 'U1rez.txt', 'w') as f:
        print(veleveliu, file=f)

        # Užduotyje nurodyta likusių juostelių skaičių surašyti nurodyta spalvų tvarka G,
        # R, Z.
        for spalva in 'GZR':
            # Skaičiuojame kiek juostelių liko kiekvienoje krūvelėje, atimdami pradinį
            # krūvelėje buvusių juostelių skaičių ir vėliavėlėms reikalingų juostelių
            # skaičiaus.
            liko = kruveles[spalva] - veleveliu * 2
            print(f'{spalva} = {liko}', file=f)
