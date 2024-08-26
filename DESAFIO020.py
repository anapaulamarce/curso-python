# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao dos trabalhos dos alunos.
# Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('digite o nome do aluno numero 1: '))
n2 = str(input('digite o nome do aluno número 2: '))
n3 = str(input('digite o nome do aluno numero 3: '))
n4 = str(input('digite o nome do aluno número 4: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentacao sera: {}'.format(lista))