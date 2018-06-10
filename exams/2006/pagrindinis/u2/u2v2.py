"""
With statement
Lambda funkcija.
List comprehension.
f-string
_ žymimi nereikšmingi kintamieji
zip() tuple unpacking
"""
from os.path import join

SIMBOLIŲ_KIEKIS_PAVADINIMUI = 15


def nuskaityti_duomenis_iš_failo(duomenų_direktorija):
    with open(join(duomenų_direktorija, "Duom2.txt"), 'r', encoding='utf-8') as failas:
        return failas.read().split("\n")


def rezultato_įrašymas_į_failą(rezultatų_masyvas, duomenų_direktorija):
    with open(join(duomenų_direktorija, "Rez2.txt"), 'w', encoding='utf-8') as failas:
        masyvas_konvertuotas_į_tekstą = "\n".join(rezultatų_masyvas)
        failas.write(masyvas_konvertuotas_į_tekstą)


def apskaičiuoti_sustojimų_laikus(duomeų_eilutės):
    laikas = lambda atstumas, greitis: round(atstumas / greitis * 60)

    _, vidutinis_greitis, išvykimo_valanda, išvykimo_minutės = list(map(int, duomeų_eilutės[0].split()))
    išvykimas_minutėmis = išvykimo_valanda * 60 + išvykimo_minutės

    miestai = [eilutė[:SIMBOLIŲ_KIEKIS_PAVADINIMUI] for eilutė in duomeų_eilutės[1:]]
    kelionių_trukmės = [laikas(float(eilutė[SIMBOLIŲ_KIEKIS_PAVADINIMUI:]), vidutinis_greitis)
                        for eilutė in duomeų_eilutės[1:]]
    atvykimai_minutėmis = [išvykimas_minutėmis + sum(kelionių_trukmės[:i]) for i in range(1, len(kelionių_trukmės) + 1)]

    return [f"{miestas}{atvykimas_minutėmis//60} val. {atvykimas_minutėmis%60} min." for
            miestas, atvykimas_minutėmis in zip(miestai, atvykimai_minutėmis)]


def main(duomenų_direktorija):
    duomeų_eilutės = nuskaityti_duomenis_iš_failo(duomenų_direktorija)
    rezultatų_masyvas = apskaičiuoti_sustojimų_laikus(duomeų_eilutės)
    rezultato_įrašymas_į_failą(rezultatų_masyvas, duomenų_direktorija)
