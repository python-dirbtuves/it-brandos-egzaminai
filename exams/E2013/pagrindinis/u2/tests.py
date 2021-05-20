from exams.E2013.pagrindinis.u2 import u2
from exams.testing import read
from exams.testing import write


def test(path):
    write(path / 'U2.txt', [
        '15',
        'Vilnius             Vilniaus     541278',
        'Dusetos             Utenos       4211',
        'Alytus              Alytaus      69859',
        'Druskininkai        Alytaus      16890',
        'Ignalina            Utenos       6307',
        'Kavarskas           Utenos       753',
        'Lazdijai            Alytaus      5027',
        'Simnas              Alytaus      1940',
        'Trakai              Vilniaus     5504',
        'Utena               Utenos       33086',
        'Veisiejai           Alytaus      1673',
        'Vievis              Vilniaus     5246',
        'Lentvaris           Vilniaus     11832',
        'Visaginas           Utenos       28438',
        'Zarasai             Utenos       8001 ',
    ])
    u2.main(path)
    assert read(path / 'U2rez.txt') == [
        '3',
        'Utenos        753 80796',
        'Alytaus       1673 95389',
        'Vilniaus      5246 563860',
    ]
