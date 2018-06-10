"""
"It is often easier to ask for forgiveness than to ask for permission." - Grace Hopper
Python dictionary
Try/catch
Lambda funkcijos.
Sortinimas su key.
Context manager failų skaitymui/rašymui.
List comprehension
zip() tuple unpacking
"""

DUOMENU_FAILAS = "U1.txt"
NAUJOS_EILUTĖS_SIMBOLIS = "\n"
RAŠYMO_REŽIMAS = 'w'
SKAITYMO_REŽIMAS = 'r'
TEKSTO_KODUOTĖ = 'utf-8'
REZULTATŲ_FAILAS = "U1rez.txt"


def nuskaityti_duomenis_iš_failo(duomenu_failas):
    with open(duomenu_failas, SKAITYMO_REŽIMAS, encoding=TEKSTO_KODUOTĖ) as failas:
        return [[int(skaičius) for skaičius in grybavimas.split()] for grybavimas in
                failas.read().split(NAUJOS_EILUTĖS_SIMBOLIS)[1:]]


def rezultato_įrašymas_į_failą(rezultatų_masyvas):
    with open(REZULTATŲ_FAILAS, RAŠYMO_REŽIMAS, encoding=TEKSTO_KODUOTĖ) as failas:
        masyvas_konvertuotas_į_tekstą = NAUJOS_EILUTĖS_SIMBOLIS.join(rezultatų_masyvas)
        failas.write(masyvas_konvertuotas_į_tekstą)


def main():
    grybavimai = nuskaityti_duomenis_iš_failo(DUOMENU_FAILAS)
    rezultatai = {}
    for grybavimas in grybavimai:
        try:
            rezultatai[grybavimas[0]] = [ankstesnis_laimikis + vėlesnis_laimikis for
                                         ankstesnis_laimikis, vėlesnis_laimikis in
                                         zip(rezultatai[grybavimas[0]], grybavimas[1:])]
        except KeyError:
            if sum(grybavimas[1:]):
                rezultatai[grybavimas[0]] = grybavimas[1:]

    rezultatai = sorted([[diena] + grybai for diena, grybai in rezultatai.items()], key=lambda x:x[0])
    daugiausia = max(rezultatai, key=lambda x: sum(x[1:]))
    rezultatai.append([daugiausia[0], sum(daugiausia[1:])])
    rezultato_įrašymas_į_failą([" ".join([str(r) for r in rez]) for rez in rezultatai])

if __name__ == '__main__':
    main()