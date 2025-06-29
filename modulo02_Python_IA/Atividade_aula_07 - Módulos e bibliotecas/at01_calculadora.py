# ATIVIDADE PRÁTICA 1

# Crie um programa que será uma calculadora.

# Nesta calculadora você deverá ter um módulo para as
# operações matemáticas, o arquivo principal deverá
# conter apenas um menu de escolha para o usuário

# (soma, subtração, multiplicação e divisão).


def calculadora (num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        if num2 == 0:
            return 'O divisor não pode ser zero, faça a conta de novo!'
        else:
            return num1 / num2
    elif operacao == 4:
        return num1 * num2
    else:
        return 'Operador inválido, comece de novo!'