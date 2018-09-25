
import os

path = os.path.abspath("\\\\seaeb-wr\WR\\1_Seattle\HWAS\DATA\Cedars-Sinai Health System\Extracts\Anthem\\test\\test.txt")

print(path)

with open(path, 'w+') as f:
    f.write('This one is more manual\n')
    print("This is from a print statement", file=f)
    print('a','b','c','d','e', sep='*')
    f.close()