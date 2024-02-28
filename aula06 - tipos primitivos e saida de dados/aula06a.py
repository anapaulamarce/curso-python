n1 = int(input('Digite um valor: ')) ## a variavel precisa ser especificada na pergunta
n2 = int(input('Digite outro: '))
s = n1 + n2

## print('A soma entre', n1, 'e', n2, 'vale', s),  esse é o formato antigo do python
print('A soma entre {} e {} vale {}'.format(n1, n2, s))