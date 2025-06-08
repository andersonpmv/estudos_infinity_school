# DESAFIO PRÁTICO
# Gerenciamento de Compras de Produtos
# Você foi contratado para desenvolver um programa simples para
# auxiliar em um processo de compra de produtos. O programa deve
# permitir ao usuário inserir o nome e o preço de vários produtos,
# perguntando se deseja continuar inserindo mais produtos após cada
# entrada. Ao final, o programa deve fornecer um resumo da compra,
# incluindo:

# A) O total gasto na compra.
# B) A quantidade de produtos que custam mais de R$1000.
# C) O nome do produto mais barato.
# Desenvolva o programa em Python utilizando conceitos de
# entrada/saída de dados, condicionais e laços de repetição.

produtos = []

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))

    produto = {
        nome: preco
    }
    produtos.append(produto)
    continuar = input('Deseja inserir outro produto, "s" sim e "n" não').lower()
    if continuar == 'n':
        break
produtos = sorted(produtos, key=lambda item: list(item.values())[0])

mais_caro = max(produtos, key=lambda item: list(item.values())[0])
mais_barato = min(produtos, key=lambda item: list(item.values())[0])

nome_caro = list(mais_caro.keys())[0]
preco_caro = list(mais_caro.values())[0]

nome_barato = list(mais_barato.keys())[0]
preco_barato = list(mais_barato.values())[0]

print(produtos)

print(f"Mais caro: {nome_caro} - R${preco_caro:.2f}")
print(f"Mais barato: {nome_barato} - R${preco_barato:.2f}")