## Crie um programa que leia o nome de uma cidade e diga se
## ela começa ou nao com o nome "SANTO".

cid = str(input('Em que cidade voce nasceu?' )).strip() ## strip elimina os espaços
print(cid[0:5].upper() == 'SANTO') ## vai de 0 a 5, se nao colocar o 0 na frente, começa do começo
## .upper, fiz a conversao para maiusculo