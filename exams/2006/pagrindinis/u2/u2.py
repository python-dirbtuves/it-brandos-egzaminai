from os.path import join

SIMBOLIŲ_KIEKIS_MIESTO_PAVADINIMUI = 15


def nuskaityti_duomenis_iš_failo(duomenų_direktorija):
    failas = open(join(duomenų_direktorija, "Duom2.txt"), 'r', encoding='utf-8')
    duomenys = failas.read()
    failas.close()
    return duomenys

def rezultato_įrašymas_į_failą(rezultatų_masyvas, duomenų_direktorija):
    failas = open(join(duomenų_direktorija, "Rez2.txt"), 'w', encoding='utf-8')
    masyvas_konvertuotas_į_tekstą = "\n".join(rezultatų_masyvas)
    failas.write(masyvas_konvertuotas_į_tekstą)
    failas.close()


def apskaičiuoti_sustojimų_laikus(duomenų_failo_tekstas):
    def laikas(atstumas, greitis):
        return round(atstumas / greitis * 60)

    def apskaičiuoti_atvykimo_į_stotelę_laiką(
        autobuso_vidutinis_greitis,
        ankstesnio_sustojimo_valanda,
        ankstesnio_sustojimo_minutės,
        atstumas):

        sustojimo_minutės = ankstesnio_sustojimo_minutės + laikas(atstumas, autobuso_vidutinis_greitis)

        if sustojimo_minutės >= 60:
            sustojimo_valanda = ankstesnio_sustojimo_valanda + sustojimo_minutės // 60
            sustojimo_minutės = sustojimo_minutės % 60
        else:
            sustojimo_valanda = ankstesnio_sustojimo_valanda

        return sustojimo_valanda, sustojimo_minutės

    # Suskaldome tekstą į masyvą, naudodami naujos eilutės simbolį \n, kaip skaldymo ženklą
    teksto_eilučių_masyvas = duomenų_failo_tekstas.splitlines()

    # Pirmos eilutės elementai suskaldomi į masyvą su split() funkcija ir reikšmės priskiriamos kintamiesiems
    stotelių_skaičius, vidutinis_greitis, išvykimo_valanda, išvykimo_minutės = teksto_eilučių_masyvas[0].split()

    rezultatų_masyvas = []
    ankstesnio_sustojimo_valanda = išvykimo_valanda
    ankstesnio_sustojimo_minutės = išvykimo_minutės

    for eilutė in teksto_eilučių_masyvas[1:]:
        miestas, atstumas = eilutė[:SIMBOLIŲ_KIEKIS_MIESTO_PAVADINIMUI], eilutė[SIMBOLIŲ_KIEKIS_MIESTO_PAVADINIMUI:]

        atvykimo_valanda, atvykimo_minutės = apskaičiuoti_atvykimo_į_stotelę_laiką(
            float(vidutinis_greitis),
            int(ankstesnio_sustojimo_valanda),
            int(ankstesnio_sustojimo_minutės),
            float(atstumas)
        )
        rezultatų_masyvas.append(f"{miestas}{atvykimo_valanda} val. {atvykimo_minutės} min.")
        ankstesnio_sustojimo_valanda = atvykimo_valanda
        ankstesnio_sustojimo_minutės = atvykimo_minutės
    return rezultatų_masyvas


def main(duomenų_direktorija):
    duomenų_failo_tekstas = nuskaityti_duomenis_iš_failo(duomenų_direktorija)
    rezultatų_masyvas = apskaičiuoti_sustojimų_laikus(duomenų_failo_tekstas)
    rezultato_įrašymas_į_failą(rezultatų_masyvas, duomenų_direktorija)
