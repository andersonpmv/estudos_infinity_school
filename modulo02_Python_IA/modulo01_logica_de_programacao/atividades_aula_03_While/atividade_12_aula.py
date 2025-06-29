# Atividade 12:
# Senha Correta:
# Desenvolva um programa que peça ao usuário para digitar uma
# senha e continue pedindo até que a senha correta (previamente
# definida) seja inserida.

senha = '1234'
validacao = input ('Digite a senha: ')

while senha != validacao:
    validacao = input('Senha errada, digite novamente: ')
else:
    print(f'Senha certa!')