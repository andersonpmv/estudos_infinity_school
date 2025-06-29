# ATIVIDADE PRÁTICA 1

# Crie um programa que solicita ao usuário que insira três
# notas e, em seguida, calcule a média dessas notas
# usando uma função. A função deve receber as três
# notas como argumentos e retornar a média. Por fim, o
# programa deve imprimir a média calculada.

def media (a, b, c):
    media = (a + b + c) / 3
    return media
notas = []

for nota in range(1, 4):
    entrada = float(input(f'Digite a {nota}° nota: '))
    notas.append(entrada)

resultado = media(notas[0], notas[1], notas[2])

print(f'A média é {resultado:.2f}')
