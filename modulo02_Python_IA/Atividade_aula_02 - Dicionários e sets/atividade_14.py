# ATIVIDADE PRÁTICA 14

# Crie um programa que receba uma lista de números e
# remova todas as duplicatas usando um conjunto (set). Em
# seguida, exiba a lista original e a lista sem duplicatas.

numero = []
while True:
    entrada = int(input('Digite um número ou "-1" para sair: '))
    if entrada == -1:
        break
    numero.append(entrada)
sem_repetidos = set(numero)
print(f'lista: {numero}\nset: {sem_repetidos}')