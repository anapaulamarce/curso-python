## Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: R$'))
novop = preco - (preco * 5 / 100) ## 5 por cento de 100

print('O valor do produto sem desconto é R${:.2f} e com desconto é R${:.2f}'.format(preco, novop))
