import argparse

parser = argparse.ArgumentParser(description='dada')
parser.add_argument('dadada', type=str)
arg = parser.parse_args()
with open(f'{arg.dadada}') as file:
    lines = file.readlines()
    with open(f'{arg.dadada}', 'w') as file:
        for i, line in enumerate(lines, 1):
            if len(line) != 0:
                string = str(str(i) + ': ' + str(line))
                file.write(string)
            else:
