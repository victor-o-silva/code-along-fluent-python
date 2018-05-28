from array import array
from random import random

SIZE = 100

gen = (random() for i in range(SIZE))
floats = array('d', gen)
with open('array_of_floats.bin', 'wb') as bin_file:
    floats.tofile(bin_file)

floats2 = array('d')
with open('array_of_floats.bin', 'rb') as bin_file:
    floats2.fromfile(bin_file, SIZE)

print(f'floats: {floats}')
print(f'floats2: {floats2}')
