from string import hexdigits, punctuation
from random import choice
filename = input("Entrez le nom du fichier (exemple : amogus.txt) : ")
with open(filename , 'r+') as f:
    length_chars = len(f.read())
    f.truncate(0) # need '0' when using r+
    f.write(''.join([choice(hexdigits + punctuation) for i in range(int(length_chars * 2))]))
    f.close()