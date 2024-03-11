## Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcue e mostre o comprimento da hipotenusa.

'''
co = float(input('Comprimento do cateto oposto : '))
ca = float(input(('Comprimento do cateto adjacente: ')))
hi = (co ** 2 + ca ** 2) ** (1/2)
'''

## agora feito com o import

from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hip))