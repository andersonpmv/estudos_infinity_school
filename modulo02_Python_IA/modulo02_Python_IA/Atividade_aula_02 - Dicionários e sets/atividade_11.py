# ATIVIDADE PRÁTICA 11

# Escreva um programa que recebe um dicionário e uma
# lista de chaves como entrada e verifica se todas as
# chaves da lista existem no dicionário. A função deve
# retornar True se todas as chaves existirem e False caso contrário.

lista = ['a', 'b', 'c']

dicio = {
    'a': 1,
    'b': 2,
    'd': 3
}

print(all(chave in dicio for chave in lista))
    