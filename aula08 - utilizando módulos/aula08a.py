from math import sqrt ## importar o sqrt de math

num = int(input('Digite um número: '))
raiz = sqrt(num)

## print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))  arredondar a raiz para cima
## print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))  arredondar a raiz para baixo

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
