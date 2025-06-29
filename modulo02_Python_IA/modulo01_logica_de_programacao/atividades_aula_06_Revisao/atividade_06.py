# Algoritmo de Cálculo de Desconto:
# Desenvolva um algoritmo que calcule o preço de um produto
# após aplicar um desconto. Solicite o preço original e o percentual
# de desconto.

preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite a porcentagem do desconto: '))
desconto = desconto / 100 * preco
preco = preco - desconto
print(f'O desconto é de R$ {desconto:.2f}, o valor a pagar é de R$ {preco:.2f}')