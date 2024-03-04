## Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metr = int(input('Digite um valor em metro: '))
cent = metr * 100
mil = metr * 1000

print('{} metros contém {} centímetros e {} milímetros!'.format(metr, cent, mil))