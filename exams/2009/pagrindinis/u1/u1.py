"""
Program to solve 2009 Lithuanian national exams main session first task.
Made by Ignas Kiela, 2018
"""

from typing import List


def calculate_nominals(nominals: List[int], ammount):
    """
    Calculates the required nominals for the ammount
    Uses a simple algorythm, should be self explanatory
    Requires nominal list to be sorted in descending order
    """
    for nominal in nominals:
        yield ammount // nominal
        ammount %= nominal


def output_results(nominals, ammounts, output_stream):
    """
    Outputs the results in required format
    """
    for nominal, ammount in zip(nominals, ammounts):
        output_stream.write(' '.join((str(nominal), str(ammount))) + '\n')
    output_stream.write(str(sum(ammounts)) + '\n')


def calculate_sum(nominals, ammounts):
    """
    Calculates the sum of money
    """
    return sum(
        nominal * ammount
        for nominal, ammount in zip(nominals, ammounts)
    )


def prepare_data(input_stream):
    input_stream.readline()  #Unnescesary data
    gilija_nom = [int(x) for x in input_stream.readline().split()]
    gilijos_tur = [int(x) for x in input_stream.readline().split()]

    gilijos_sum = calculate_sum(gilija_nom, gilijos_tur)

    #prepare the data for calculations
    gilija_nom.sort(reverse=True)

    return gilija_nom, gilijos_sum


def run(input_stream, output_stream):
    """
    Does the task
    """
    gilija_nom, gilijos_sum = prepare_data(input_stream)
    eglija_nom, eglijos_sum = prepare_data(input_stream)

    #calculate the results
    gilija_rez = list(calculate_nominals(eglija_nom, gilijos_sum))
    eglija_rez = list(calculate_nominals(gilija_nom, eglijos_sum))

    #output results
    output_results(eglija_nom, gilija_rez, output_stream)
    output_results(gilija_nom, eglija_rez, output_stream)


def main(path):
    with (path / 'U1.txt').open() as input_file, \
         (path / 'U1rez.txt').open('w') as output_file :
        run(input_file, output_file)
