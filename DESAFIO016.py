# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porcao inteira
# ex. Digite um numero: 6127, o numero 6.127 tem a parte inteira 6
# usar funcao do modulo math

import math
num = int(input('Insira um numero real: '))

print('Seu numero inteiro eh: {:.1f}'.format(num, math.trunc(num)))
