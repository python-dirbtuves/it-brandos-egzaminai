"""
Naudojamas context manager, failo nuskaitymui ir įrašymui į failą.
Lambda funkcija.
List comprehension.
f-string
_ žymimi nereikšmingi kintamieji
zip() tuple unpacking
"""

DUOMENU_FAILAS = "Duom2.txt"
NAUJOS_EILUTĖS_SIMBOLIS = "\n"
RAŠYMO_REŽIMAS = 'w'
SKAITYMO_REŽIMAS = 'r'
TEKSTO_KODUOTĖ = 'utf-8'
SIMBOLIŲ_KIEKIS_PAVADINIMUI = 15
REZULTATŲ_FAILAS = "Rez2.txt"
MINUTĖS_VALANDOJE = 60


def nuskaityti_duomenis_iš_failo(duomenu_failas):
    with open(duomenu_failas, SKAITYMO_REŽIMAS, encoding=TEKSTO_KODUOTĖ) as failas:
        return failas.read().split(NAUJOS_EILUTĖS_SIMBOLIS)


def rezultato_įrašymas_į_failą(rezultatų_masyvas):
    with open(REZULTATŲ_FAILAS, RAŠYMO_REŽIMAS, encoding=TEKSTO_KODUOTĖ) as failas:
        masyvas_konvertuotas_į_tekstą = NAUJOS_EILUTĖS_SIMBOLIS.join(rezultatų_masyvas)
        failas.write(masyvas_konvertuotas_į_tekstą)


def apskaičiuoti_sustojimų_laikus(duomeų_eilutės):
    laikas = lambda atstumas, greitis: round(atstumas / greitis * MINUTĖS_VALANDOJE)

    _, vidutinis_greitis, išvykimo_valanda, išvykimo_minutės = list(map(int, duomeų_eilutės[0].split()))
    išvykimas_minutėmis = išvykimo_valanda * MINUTĖS_VALANDOJE + išvykimo_minutės

    miestai = [eilutė[:SIMBOLIŲ_KIEKIS_PAVADINIMUI] for eilutė in duomeų_eilutės[1:]]
    kelionių_trukmės = [laikas(float(eilutė[SIMBOLIŲ_KIEKIS_PAVADINIMUI:]), vidutinis_greitis)
                        for eilutė in duomeų_eilutės[1:]]
    atvykimai_minutėmis = [išvykimas_minutėmis + sum(kelionių_trukmės[:i]) for i in range(1, len(kelionių_trukmės) + 1)]

    return [f"{miestas}{atvykimas_minutėmis//MINUTĖS_VALANDOJE} val. {atvykimas_minutėmis%MINUTĖS_VALANDOJE} min." for
            miestas, atvykimas_minutėmis in zip(miestai, atvykimai_minutėmis)]


def main(duomenu_failas):
    duomeų_eilutės = nuskaityti_duomenis_iš_failo(duomenu_failas)
    rezultatų_masyvas = apskaičiuoti_sustojimų_laikus(duomeų_eilutės)
    rezultato_įrašymas_į_failą(rezultatų_masyvas)


if __name__ == '__main__':
    """
    Paleidimui per komandinę eilutę. "python u2.py"
    """
    main(DUOMENU_FAILAS)
