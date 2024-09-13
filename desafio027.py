## Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
## Ex: Ana Maria de Souza
## Primeiro nome: Ana
## Ultimo nome: Souza

n = str(input('Digite seu nome completo: ')).strip() ## strip retira os espaços antes e depois
nome = n.split() ## split pega tudo e divide em pedaços separados por espaço
print('Seu primeiro nome é {}'.format(nome[0])) ## nome [0] = primeiro nome 
print('Seu último nome é {}'.format(nome[len(nome)-1])) ## len = vou saber quantas posiçoes tem o nome, -1 pois é sempre um a menos para pegar o último