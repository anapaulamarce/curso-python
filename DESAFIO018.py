# Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse angulo

# import math
# ang = float(input('Digite o angulo que voce deseja: '))
# seno = math.sin(math.radians(ang))
# print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
# cosseno = math.cos(math.radians(ang))
# print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
# tangente = math.tan(math.radians(ang))
# print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))

# ou

from math import radians, sin, cos, tan
ang = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))