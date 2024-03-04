## Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um número: '))
dob = num * 2
trip = num * 3
r = num ** (1/2)

print('O dobro do seu número é {}, seu triplo é {} e sua raiz quadrada é {}!'.format(dob, trip, r))
