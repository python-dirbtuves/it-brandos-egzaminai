DUOMENU_FAILAS = "Duom2.txt"
NAUJOS_EILUTĖS_SIMBOLIS = "\n"
RAŠYMO_REŽIMAS = 'w'
SKAITYMO_REŽIMAS = 'r'
TEKSTO_KODUOTĖ = 'utf-8'
SIMBOLIŲ_KIEKIS_MIESTO_PAVADINIMUI = 15
REZULTATŲ_FAILAS = "Rez2.txt"
MINUTĖS_VALANDOJE = 60


def nuskaityti_duomenis_iš_failo(duomenu_failas):
    failas = open(duomenu_failas, SKAITYMO_REŽIMAS, encoding=TEKSTO_KODUOTĖ)
    duomenys = failas.read()
    failas.close()
    return duomenys


def apskaičiuoti_sustojimų_laikus(duomenų_failo_tekstas):
    def laikas(atstumas, greitis):
        return round(atstumas / greitis * MINUTĖS_VALANDOJE)

    def apskaičiuoti_atvykimo_į_stotelę_laiką(
        autobuso_vidutinis_greitis,
        ankstesnio_sustojimo_valanda,
        ankstesnio_sustojimo_minutės,
        atstumas):

        sustojimo_minutės = ankstesnio_sustojimo_minutės + laikas(atstumas, autobuso_vidutinis_greitis)

        if sustojimo_minutės >= MINUTĖS_VALANDOJE:
            sustojimo_valanda = ankstesnio_sustojimo_valanda + sustojimo_minutės // MINUTĖS_VALANDOJE
            sustojimo_minutės = sustojimo_minutės % MINUTĖS_VALANDOJE
        else:
            sustojimo_valanda = ankstesnio_sustojimo_valanda

        return sustojimo_valanda, sustojimo_minutės

    # Suskaldome tekstą į masyvą, naudodami naujos eilutės simbolį \n, kaip skaldymo ženklą
    teksto_eilučių_masyvas = duomenų_failo_tekstas.split(NAUJOS_EILUTĖS_SIMBOLIS)

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


def rezultato_įrašymas_į_failą(rezultatų_masyvas):
    failas = open(REZULTATŲ_FAILAS, RAŠYMO_REŽIMAS, encoding=TEKSTO_KODUOTĖ)
    masyvas_konvertuotas_į_tekstą = NAUJOS_EILUTĖS_SIMBOLIS.join(rezultatų_masyvas)
    failas.write(masyvas_konvertuotas_į_tekstą)
    failas.close()


def main(duomenu_failas):
    duomenų_failo_tekstas = nuskaityti_duomenis_iš_failo(duomenu_failas)
    rezultatų_masyvas = apskaičiuoti_sustojimų_laikus(duomenų_failo_tekstas)
    rezultato_įrašymas_į_failą(rezultatų_masyvas)


if __name__ == '__main__':
    """
    Paleidimui per komandinę eilutę. "python u2.py"
    """
    main(DUOMENU_FAILAS)
