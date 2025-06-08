# [PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, 
# armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. 
# Após a inserção de todos os produtos e preços, 
# calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.

produtos = {}
for cont in range(5):
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    produtos[produto] = preco
preco_total = 0
for chave, valor in produtos.items():
    preco_total += valor

print(f'O preço total da compra foi de R$ {preco_total:.2f}!')