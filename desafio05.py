## Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
## Leia o valor 8, antes do 8 vem o 7 e depois do 8 vem o 9

num = int(input('Digite um número inteiro: '))
suc = num + 1
ant = num - 1

print('O seu número inteiro é {},  seu sucessor é {} e seu antecessor é {}!'.format(num, suc, ant), end='')
