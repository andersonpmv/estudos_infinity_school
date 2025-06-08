# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.

soma = 0
numero = 0
while numero >= 0:
    numero = int(input('Digite um numero negativo ou positivo: '))
    if numero > 0:
        soma += numero
        print (soma)
else:
    print(f'Digitou um numero negativo! A soma total dos numero positivos é {soma}')