## Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possíveis sobre ele

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace()) ## só tem espaços?
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalpha())
print('Está em letra maiúscula? ', a.isupper())
print('Está em letra minúscula? ', a.islower())
print('Está capitalizada? ', a.istitle()) ## esta capitalizada, nao está em maiúscula nem minúscula


