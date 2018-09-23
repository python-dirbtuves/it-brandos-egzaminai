from os.path import join


def nuskaityti_duomenis_iš_failo(duomenų_direktorija):
    failas = open(join(duomenų_direktorija, "U1.txt"), "r", encoding='utf-8')
    duomenys = failas.read()
    failas.close()
    return duomenys


def rezultato_įrašymas_į_failą(duomenų_direktorija, tekstas):
    failas = open(join(duomenų_direktorija, "Rez1.txt"), 'w', encoding='utf-8')
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


def main(duomenų_direktorija):
    duomenys = nuskaityti_duomenis_iš_failo(duomenų_direktorija)
    eilučių_masyvas = duomenys.splitlines()
    dienos_ir_grybai = susumuoti_dienų_grybų_kiekius_ignoruojant_dienas_be_grybų(eilučių_masyvas)
    rezultatai, daugiausia = surikiuoti_didėjančia_dienų_seka_bei_rasti_diena_su_didžiausiu_laimikiu(dienos_ir_grybai)
    tekstas = suformuoti_rezultatų_tekstą(rezultatai, daugiausia)
    rezultato_įrašymas_į_failą(duomenų_direktorija, tekstas)
