import argparse

parser = argparse.ArgumentParser(description='Найти файл')
parser.add_argument('origin', type=str)
arg = parser.parse_args()
with open(f'{arg.origin}') as file:
    strings = file.readlines()
    for string in strings[:10]:
        print(string, end='')
