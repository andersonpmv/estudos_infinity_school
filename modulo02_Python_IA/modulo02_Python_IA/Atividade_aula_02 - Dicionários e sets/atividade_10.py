# ATIVIDADE PRÁTICA 10

# Desenvolva um programa que recebe um dicionário, uma
# chave e um valor como entrada e adiciona a chave e o
# valor ao dicionário, atualizando o valor se a chave já existir.

dicionario = {}

while True:
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    dicionario[chave] = valor

    continuar = input('Digite "s" sair e "c" continuar: ')
    if continuar == 's':
        break
print(dicionario)