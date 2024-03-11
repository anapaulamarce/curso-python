## Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porçao inteira
## ex: Digite um número: 6.127
## O número 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Insira um número: '))

print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
