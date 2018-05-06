"""
Program to solve 2009 Lithuanian national exams main session first task.
Made by Ignas Kiela, 2018
"""


def calculate_nominals(nominals, ammount):
    """
    Calculates the required nominals for the ammount
    Uses a simple algorythm, should be self explanatory
    Requires nominal list to be sorted in descending order
    """
    result = []
    for nominal in nominals:
        result.append(ammount // nominal)
        ammount %= nominal
    return result


def output_results(nominals, ammounts, output_stream):
    """
    Outputs the results in required format
    """
    for nominal, ammount in zip(nominals, ammounts):
        output_stream.write(''.join((str(nominal), str(ammount))))
    output_stream.write(str(sum(ammounts)))


def calculate_sum(nominals, ammounts):
    """
    Calculates the sum of money
    """
    return sum(
        [nominal * ammount for nominal, ammount in zip(nominals, ammounts)])


def run(input_stream, output_stream):
    """
    Does the task
    """
    input_stream.readline()  #Unnescesary data
    gilija_nom = [int(x) for x in input_stream.readline().split()]
    gilijos_tur = [int(x) for x in input_stream.readline().split()]
    input_stream.readline()  #Unnescesary data
    eglija_nom = [int(x) for x in input_stream.readline().split()]
    eglijos_tur = [int(x) for x in input_stream.readline().split()]

    gilijos_sum = calculate_sum(gilija_nom, gilijos_tur)
    eglijos_sum = calculate_sum(eglija_nom, eglijos_tur)

    #prepare the data for calculations
    eglija_nom.sort(reverse=True)
    gilija_nom.sort(reverse=True)

    #calculate the results
    gilija_rez = calculate_nominals(eglija_nom, gilijos_sum)
    eglija_rez = calculate_nominals(gilija_nom, eglijos_sum)

    #output results
    output_results(eglija_nom, gilija_rez, output_stream)
    output_results(gilija_nom, eglija_rez, output_stream)


if __name__ == '__main__':
    input_file = open('U1.txt', 'r')
    output_file = open('U1rez.txt', 'w')
    run(input_file, output_file)
