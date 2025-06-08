# Atividade 08:
# Média de Notas:
# Desenvolva um programa que solicite as notas dos alunos até
# que o usuário digite -1. Calcule e exiba a média das notas
# inseridas.

dividir = 0
soma = 0
while True:
    notas = float(input('Digite a nota ou "-1" para sair do programa: '))
    if notas != -1:
        soma += notas
        dividir += 1
    else:
        break

print(f'A media desse aluno é: {soma/dividir}')