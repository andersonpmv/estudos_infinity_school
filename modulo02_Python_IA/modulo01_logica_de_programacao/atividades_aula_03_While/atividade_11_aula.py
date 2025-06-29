# Atividade 11:
# Entrada Válida:
# Crie um programa que solicite ao usuário um número entre 1 e 10.
# Continue pedindo até que o usuário forneça um valor válido.

numero = int(input('Digite um numero entre 1 e 10: '))
while numero < 1 or numero > 10:
    numero = int(input('Digitou um numero errado, digite de novo:'))
else:
    print(f'Parabéns, vc digitou um numero certo: {numero}')