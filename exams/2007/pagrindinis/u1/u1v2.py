"""
"It is often easier to ask for forgiveness than to ask for permission." - Grace Hopper
Python dictionary
Try/catch
Lambda funkcijos.
Sortinimas su key.
With statment
List comprehension
zip() tuple unpacking
"""
from os.path import join


def nuskaityti_duomenis_iš_failo(duomenų_direktorija):
    with open(join(duomenų_direktorija, "U1.txt"), 'r', encoding='utf-8') as failas:
        return [[int(skaičius) for skaičius in grybavimas.split()] for grybavimas in list(failas)[1:]]


def rezultato_įrašymas_į_failą(rezultatų_masyvas, duomenų_direktorija):
    with open(join(duomenų_direktorija, "U1rez.txt"), 'w', encoding='utf-8') as failas:
        failas.write("\n".join(rezultatų_masyvas))


def main(duomenų_direktorija):
    grybavimai = nuskaityti_duomenis_iš_failo(duomenų_direktorija)
    rezultatai = surinkti_duomenis_apie_grybavimą_pagal_dienas_bei_rasti_diena_su_didžiausiu_laimikiu(grybavimai)
    rezultato_įrašymas_į_failą([" ".join([str(r) for r in rez]) for rez in rezultatai], duomenų_direktorija)


def surinkti_duomenis_apie_grybavimą_pagal_dienas_bei_rasti_diena_su_didžiausiu_laimikiu(grybavimai):
    rezultatai = {}
    for grybavimas in grybavimai:
        try:
            rezultatai[grybavimas[0]] = [ankstesnis_laimikis + vėlesnis_laimikis for
                                         ankstesnis_laimikis, vėlesnis_laimikis in
                                         zip(rezultatai[grybavimas[0]], grybavimas[1:])]
        except KeyError:
            if sum(grybavimas[1:]):
                rezultatai[grybavimas[0]] = grybavimas[1:]
    rezultatai = sorted([[diena] + grybai for diena, grybai in rezultatai.items()], key=lambda x: x[0])
    didžiausias_laimikis = max(rezultatai, key=lambda x: sum(x[1:]))
    rezultatai.append([didžiausias_laimikis[0], sum(didžiausias_laimikis[1:])])
    return rezultatai
