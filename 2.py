import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("a", type=str)
parser.add_argument("b", type=str)
args = parser.parse_args()
def s(a,b):
    if os.path.exists(a) and os.path.exists(b):
       with open(f'{args.a}') as file:
           with open(f'{args.b}') as file1:
                while True:
                    ln = file.readline()
                    print(ln.strip())
                    if not ln:
                        break
                while True:
                    ln = file1.readline()
                    print(ln.strip())
                    if not ln:
                        break
       return ln
    else:
        print("Файла нет")
s(args.a, args.b)
