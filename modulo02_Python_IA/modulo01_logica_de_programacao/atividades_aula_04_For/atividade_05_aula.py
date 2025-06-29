# Atividade 05:
# Contagem de Números Positivos e Negativos:
# Escreva um programa que solicite ao usuário 10 números e use um
# laço for com uma condicional para contar quantos são positivos e
# quantos são negativos.

positivo = 0
negativo = 0

for i in range(1,11):
    numero = int(input('Digite um número negativo ou positivo: '))
    if numero % 2 == 0:
        positivo += 1
    else:
        negativo += 1
print(f'A quantidade de positivos é {positivo} e negativos é {negativo}')