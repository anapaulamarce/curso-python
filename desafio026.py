## Faça um programa que leia uma frase pelo teclado e mostre:
## Quantas vezes aparece a letra "A"
## Em que posiçao ela aparece a primeira vez
## Em que posiçao ela aparece a última vez

frase = str(input('Digite uma frase: ')).upper().strip() ## converte essa str para maiusculo, strip tira os espaços
print('A letra A aparece {} vezes na frase.'.format((frase.count('A')))) ## conta quantos A maiusculo tem
print('A primeira letra A apareceu na posiçao {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posiçao {}'. format(frase.rfind('A')+1))
