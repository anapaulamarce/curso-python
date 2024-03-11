## Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang)) ## converter o grau para radiano
cose = cos(radians(ang))
tang = tan(radians(ang))

print('Ângulo {}º'.format(ang))
print('Seu seno é {:.2f}'.format(sen))
print('Seu coseno é {:.2f}'.format(cose))
print('Sua tangente é {:.2f}'.format(tang))
