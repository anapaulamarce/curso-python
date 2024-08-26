## Crie um programa que leia o nome completo de uma pessoa e mostre:
## O nome com todas as letras maiusculas e minusculas
## Quantas letras ao todo (sem considerar espaços)
## Quantas letras tem o primeiro nome 

nome = str(input('Digite seu nome completo: ')).strip() ## strip elimina os espaços antes e depois do nome, mas nao elimina o espaço do meio
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) ## quantidade de letras com o espaço, mas elimina quantos espaços tem
## print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))