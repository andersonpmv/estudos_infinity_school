# Cálculo de IMC:
# Crie um programa que calcule o Índice de Massa Corporal (IMC).
# Peça ao usuário para digitar seu peso e altura, armazene em
# variáveis e calcule o IMC.

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / altura **2

print(f'O IMC é {imc:.2f}')