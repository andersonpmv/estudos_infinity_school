# Categoria de Idade:
# Desenvolva um programa que peça a idade do usuário e
# informe se ele é criança, adolescente, adulto ou idoso.

idade = int(input('Digite sua idade: '))

if idade > 59:
    print('Idoso')
elif idade > 17:
    print('Adulto')
elif idade > 13:
    print('Adolescente')
else:
    print('Criança')