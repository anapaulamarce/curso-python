# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
n1 = str(input('digite o nome do aluno numero 1: '))
n2 = str(input('digite o nome do aluno número 2: '))
n3 = str(input('digite o nome do aluno numero 3: '))
n4 = str(input('digite o nome do aluno número 4: '))
n5 = random.choice([n1 , n2, n3 , n4])
print('o aluno sorteado para limpar o quadro foi: {}'.format(n5))

