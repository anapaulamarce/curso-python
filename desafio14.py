## Faça um programa que leia a temperatura em graus Celcius e converta ela para fahrenheit

cel = float(input('Insira a temperatura em ºC: '))
fah = (cel * 1.8) + 32

print('A temperatura de {}ºC corresponde a {:.3f}:ºF'.format(cel, fah))