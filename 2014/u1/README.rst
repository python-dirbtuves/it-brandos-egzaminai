I užduotis. Balsavimo rezultatai
================================

Įmonėje, sudarytoje iš keleto skyrių, renkamas vienas iš trijų logotipų.
Parengtos tokios darbuotojų apklausos taisyklės:

1. Kiekvienas skyriaus darbuotojas (išskyrus direktorių) atiduoda savo balsą už
   kurį nors vieną logotipą.

2. Atskirai kiekviename skyriuje suskaičiavus darbuotojų balsus, daugiausia
   balsų surinkusiam logotipui skiriami keturi taškai, jei du geriausiai
   įvertinti logotipai surenka vienodai balsų – jiems skiriama po du taškus, o
   jei balsai pasiskirsto po lygiai – taškų tame skyriuje neskiriama.

3. Atskirai susumuojami pirmo, antro ir trečio logotipų visuose skyriuose gauti
   taškai.

4. Jei du ar trys geriausi logotipai surenka po vienodai taškų, prie kiekvieno
   logotipo taškų sumos pridedami direktoriaus skirti taškai. Direktorius
   vienam iš logotipų skiria 3 taškus, kitam – 2, o likusiam – 1 tašką.

5. Nugali tas logotipas, kuris surenka daugiausia taškų.

   Parašykite programą, kuri nustatytų:

   - kiek iš viso balsų ir taškų gavo kiekvienas logotipas,

   - kuris iš logotipų buvo išrinktas.

Pradiniai duomenys
------------------

Duomenys yra tekstiniame faile ``U1.txt``:

- pirmoje eilutėje yra įmonės skyrių skaičius ``k (1<=k<=10)``,

- kitose ``k`` eilučių yra už pirmąjį, antrąjį ir trečiąjį logotipus
  kiekviename skyriuje skirti balsai,

- paskutinėje eilutėje yra už pirmąjį, antrąjį ir trečiąjį logotipą atiduoti
  direktoriaus taškai (trys skirtingi skaičiai nuo 1 iki 3).

Rezultatai
----------

Tekstiniame faile ``U1rez.txt`` rezultatus įrašykite tokia tvarka:

- pirmoje eilutėje trims logotipams tekusių balsų skaičiai,

- antroje eilutėje trims logotipams tekusių taškų skaičiai,

- trečioje eilutėje – laimėjusio logotipo numeris.

Nurodymai
---------

- Parašykite taškų apskaičiavimo viename skyriuje procedūrą.

- Parašykite funkciją, nustatančią geriausią logotipą visoje įmonėje.

- Programoje nenaudokite sakinių, skirtų darbui su ekranu.

Duomenų ir rezultatų pavyzdys
-----------------------------

+--------------------------+--------------------------------------------+
| Duomenų failo pavyzdys   | Paaiškinimai                               |
+==========================+============================================+
| ::                       | Pirmoje eilutėje – skyrių skaičius.        |
|                          |                                            |
|                          | Kitose eilutėse – atitinkami kiekvieno     |
|     6                    | skyriaus darbuotojų balsai, atiduoti       |
|     15 10 22             | atitinkamai už už pirmąjį, antrąjį ir      |
|     15 40 13             | trečiąjį logotipus.                        |
|     23 26 26             |                                            |
|     110 30 58            | Paskutinėje eilutėje – atitinkamai už      |
|     33 33 32             | pirmąjį, antrąjį ir trečiąjį logotipą      |
|     0 56 0               | atiduoti direktoriaus taškai.              |
|     2 1 3                |                                            |
|                          |                                            |
|                          |                                            |
+--------------------------+--------------------------------------------+


+--------------------------+--------------------------------------------+
| Rezultatų failo pavyzdys | Paaiškinimai                               |
+==========================+============================================+
| ::                       | Pirmoje eilutėje trims logotipams tekusių  |
|                          | balsų skaičiai.                            |
|     196 195 151          |                                            |
|     6 12 6               | Antroje eilutėje trims logotipams tekusių  |
|     2                    | taškų skaičiai.                            |
|                          |                                            |
|                          | Trečioje eilutėje – laimėjusio logotipo    |
|                          | numeris.                                   |
|                          |                                            |
|                          |                                            |
|                          |                                            |
+--------------------------+--------------------------------------------+

Programos vertinimas
--------------------

+---------------------------------------------------+--------+------------------------------+
| Vertinimo kriterijai                              | Taškai | Pastabos                     |
+===================================================+========+==============================+
| Testai                                            | 17     | Visi taškai skiriami, jeigu  |
|                                                   |        | programa pateikia            |
|                                                   |        | teisingus visų testų         |
|                                                   |        | rezultatus.                  |
+---------------------------------------------------+--------+------------------------------+
| Teisingai skaitomi duomenys iš failo.             | 2      | Vertinama tada, kai          |
+---------------------------------------------------+--------+ neskiriama taškų už testus.  |
| Teisingai išvedami rezultatai į failą.            | 2      |                              |
+---------------------------------------------------+--------+                              |
| Teisingai nustatomas taškų skaičius viename       | 8      |                              |
| skyriuje.                                         |        |                              |
+---------------------------------------------------+--------+                              |
| Teisingai nustatomas išrinktas logotipas.         | 4      |                              |
+---------------------------------------------------+--------+                              |
| Teisingos kitos procedūros [1]_ ir funkcijos,     | 1      |                              |
| jeigu jų yra, ir pagrindinė programa [2]_.        |        |                              |
+---------------------------------------------------+--------+------------------------------+
| Sukurta ir naudojama taškų apskaičiavimo viename  | 2      | Visada vertinama.            |
| skyriuje procedūra.                               |        |                              |
+---------------------------------------------------+--------+                              |
| Sukurta ir naudojama funkcija, nustatanti         | 2      |                              |
| geriausią logotipą.                               |        |                              |
+---------------------------------------------------+--------+                              |
| Teisingai aprašyti kintamieji ir kitos duomenų    | 2      |                              |
| saugojimo struktūros.                             |        |                              |
+---------------------------------------------------+--------+                              |
| Prasmingai pavadinti kintamieji. Komentuojamos    | 1      |                              |
| programos dalys.                                  |        |                              |
+---------------------------------------------------+--------+                              |
| Laikomasi rašybos taisyklių. Išlaikomas vientisas | 1      |                              |
| programos rašymo stilius, nėra sakinių, skirtų    |        |                              |
| darbui su ekranu.                                 |        |                              |
+---------------------------------------------------+--------+------------------------------+
| Iš viso taškų                                     | 25     |                              |
+---------------------------------------------------+--------+------------------------------+
|                                                   |        |                              |
+---------------------------------------------------+--------+------------------------------+

.. [1] C++ programavimo kalboje procedūra suprantama kaip funkcija.
.. [2] C++ programavimo kalboje pagrindinė programa suprantama kaip main() funkcija.


**Nepamirškite** savo darbo rezultatų įrašyti į kompiuterio standžiojo disko
aplanką ``C:\Egzaminas``, suteikdami failams vardus, sudarytus pagal šabloną:
``R01_1.pas`` (``R01_1.cpp``) (``R`` – grupė (1 simbolis), eilės numeris (2
simboliai, pvz., ``06``; ``14``), atskiras skaitmuo – praktinės užduoties
numeris). Kitaip įvardyti failai nebus vertinami. Failo pavadinime ar jo tekste
neturi būti užrašų ar kitokių ženklų, kurie leistų identifikuoti darbo autorių
(pvz., vardo, pavardės, mokyklos ir t. t.).
