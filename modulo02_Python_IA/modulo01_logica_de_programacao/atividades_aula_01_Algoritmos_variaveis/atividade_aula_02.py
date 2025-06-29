# Atividade 02: Crie um programa que peça ao usuário para digitar:
# 1.Seu nome;
# 2.Sua idade;
# 3.Sua altura;
# 4.Em seguida, imprima esses valores e seus respectivos tipos.

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))
print(f'{nome} = {type(nome)}')
print(f'{idade} = {type(idade)}')
print(f'{altura} = {type(altura)}')