## Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do seu salário: R$'))
novosal = salario + (salario * 15 / 100) ## 15 por cento de 100

print('O seu novo salário com 15% de aumento é R${:.2f}'.format(novosal))