# ATIVIDADE PRÁTICA 9

# Escreva um programa que percorra as chaves e valores
# de um dicionário separadamente e os exiba.

nome_idade = {
    'Anderson': 31,
    'Catarina': 36
}

for chave, elemento in nome_idade.items():
    print(f'{chave}:{elemento}')