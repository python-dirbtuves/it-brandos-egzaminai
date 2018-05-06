import u1


def test_a_pvz(path):
    (path / 'U1.txt').write(
        '2 3',
        '0 128 0',
        '255 0 0',
        '255 255 255',
        '255 255 0',
        '255 0 0',
        '255 255 0'
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '008000;FF0000;FFFFFF',
        'FFFF00;FF0000;FFFF00'
    ]
