import os

os.system ('cls')

primeira_nota= int(input('digite sua peimeira nota: '))
segunda_nota= int(input('digite sua segunda nota: ') )
falta = int(input('digite seu numero de faltas: '))


media = (primeira_nota + segunda_nota) / 2

if media >=7 and falta < 40:
    resultado = (' aprovado: ')
else:
    resultado = ('reprovado')

print(f'media  {media}' )
print(f'falta  {falta} ')
print(f'primeira_nota  {primeira_nota}')
print(f'segunda_nota {segunda_nota}')
print(resultado)
