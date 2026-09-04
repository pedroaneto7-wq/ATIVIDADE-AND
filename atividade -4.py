import os


os. system ('cls')


numero = int(input('digite o numero: '))

if numero >= 0 and numero <= 10:
    print(f'{numero} esta entre 0 e 10')
else:
    print(f'{numero} não esta entre 0 e 10')