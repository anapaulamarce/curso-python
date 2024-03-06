## Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
## Considere US$1,00 = 4,94

val = float(input('Insira o valor que você tem na carteira: ')) ## usamos o float 
dol = val / 4.94

print('Essa pessoa pode comprar {:.2f} dólares'.format(dol)) ## :.2f é para mostrar duas casas decimais