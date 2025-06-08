# Faça um programa que, dado um conjunto de N
# números, determine o menor valor, o maior valor e a
# soma dos valores.
soma = 0
primeira_vez = True

while True:
    numero = int(input('Digite um número positivo ou "-1" para sair: '))

    if numero == -1:
        break
    if primeira_vez:
        maior = numero
        menor = numero
        primeira_vez = False
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

    soma += numero
if primeira_vez:
    print('Nenhum número digitado!')
else:
    print(f'A soma dos números é {soma}, o maior é {maior} e o menor é {menor}')