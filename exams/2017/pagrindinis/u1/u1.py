def main(path):
    with open(path / 'U1.txt') as f:
        data = f.readlines()
        height, width = [int(i) for i in data[0].split(' ')]
        data = data[1:]
        answer = ''
        for index, line in enumerate(data):
            answer += ''.join(('0', '')[int(i) > 16] + hex(int(i))[2:].upper() for i in line.split(' ')) + (';', '\n')[(index + 1) % width == 0]

    with open(path / 'U1rez.txt', 'w') as f:
        f.write(answer)
