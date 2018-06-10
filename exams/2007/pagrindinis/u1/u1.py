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
    failas = open(duomenu_failas, SKAITYMO_REŽIMAS, encoding=TEKSTO_KODUOTĖ)
    duomenys = failas.read()
    failas.close()
    return duomenys


def rezultato_įrašymas_į_failą(tekstas):
    failas = open(REZULTATŲ_FAILAS, RAŠYMO_REŽIMAS, encoding=TEKSTO_KODUOTĖ)
    failas.write(tekstas)
    failas.close()


def suformuoti_rezultatų_tekstą(rezultatai, daugiausia):
    tekstas = ""
    for r in rezultatai:
        tekstas += f"{r[0]} {r[1]} {r[2]} {r[3]}\n"
    tekstas += f"{daugiausia[0]} {daugiausia[1]}"
    return tekstas


def surikiuoti_didėjančia_dienų_seka_bei_rasti_diena_su_didžiausiu_laimikiu(dienos_ir_grybai):
    rezultatai = []
    for diena, grybai in dienos_ir_grybai.items():
        if len(rezultatai) == 0:
            # Pirmą kartą pridėti dieną su grybais ir išsaugoti ją, kaip didžiausio laimikio dieną
            rezultatai.append([diena] + grybai)
            daugiausia = [diena, sum(grybai)]
        elif diena < rezultatai[-1][0]:
            # Jeigu paskutinis įrašas turi dieną su didesniu skaičiumi, nei dabartinės interacijos diena
            for i in range(len(rezultatai)):
                # Interuojame per rezultatus ir ieškome pirmos didesnės dienos reikšmęs, prieš kurią įstatysime naują įrašą
                if rezultatai[i][0] > diena:
                    rezultatai.insert(i, [diena] + grybai)
                    break
            daugiausia = sukeisti_didžiausią_jei_laimikis_geresnis(daugiausia, diena, grybai)
        else:
            # Tiesiog pridedame įrašą į sąrašą ir patikriname ar laimikis nėra didesnis už ankstesnį išsaugotą
            rezultatai.append([diena] + grybai)
            daugiausia = sukeisti_didžiausią_jei_laimikis_geresnis(daugiausia, diena, grybai)
    return rezultatai, daugiausia


def sukeisti_didžiausią_jei_laimikis_geresnis(daugiausia, diena, grybai):
    suma = sum(grybai)
    if suma > daugiausia[1]:
        daugiausia = [diena, sum(grybai)]
    return daugiausia


def susumuoti_dienų_grybų_kiekius_ignoruojant_dienas_be_grybų(eilučių_masyvas):
    grybavimai = eilučių_masyvas[1:]  # Pasidarome masyvo kopiją be pirmos eilutės, kurioje nurodytas grybavimų skaičius
    dienos_ir_grybai = {}
    for grybavimas in grybavimai:
        diena, baravykai, raudonikės, lepšiai = grybavimas.split()
        diena = int(diena)
        if diena not in dienos_ir_grybai:
            # Jei buvo rasta grybų, sukurti naują įrašą grybavimo dienai, su grybų masyvo reikšme
            if int(baravykai) > 0 or int(raudonikės) > 0 or int(lepšiai) > 0:
                dienos_ir_grybai[diena] = [int(baravykai), int(raudonikės), int(lepšiai)]
        else:
            # Jei žodyne jau yra dienos raktas, tada susumuoti grybų laimikius
            dienos_ir_grybai[diena][0] += int(baravykai)
            dienos_ir_grybai[diena][1] += int(raudonikės)
            dienos_ir_grybai[diena][2] += int(lepšiai)
    return dienos_ir_grybai


def main():
    duomenys = nuskaityti_duomenis_iš_failo(DUOMENU_FAILAS)
    eilučių_masyvas = duomenys.split(NAUJOS_EILUTĖS_SIMBOLIS)
    dienos_ir_grybai = susumuoti_dienų_grybų_kiekius_ignoruojant_dienas_be_grybų(eilučių_masyvas)
    rezultatai, daugiausia = surikiuoti_didėjančia_dienų_seka_bei_rasti_diena_su_didžiausiu_laimikiu(dienos_ir_grybai)
    tekstas = suformuoti_rezultatų_tekstą(rezultatai, daugiausia)
    rezultato_įrašymas_į_failą(tekstas)


if __name__ == '__main__':
    main()
