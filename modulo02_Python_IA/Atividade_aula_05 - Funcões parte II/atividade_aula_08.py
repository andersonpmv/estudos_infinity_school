# ATIVIDADE PRÁTICA 8

# Crie uma função que aceite dois números e uma
# operação (por exemplo, adição, subtração,
# multiplicação, divisão) como argumentos e use funções
# lambda para realizar a operação especificada. A função
# deve retornar o resultado da operação.

def calcular (a, b, c):
    if c == '-':
        conta = lambda a, b: a - b
    elif c == '+':
        conta = lambda a, b: a + b
    elif c == '*':
        conta = lambda a, b: a * b
    elif c == '/':
        if b == 0:
            return 'Erro: divisão por zero'
        conta = lambda a, b: a / b
    else:
        return 'Operação inválida!'
    
    return conta(a, b)
resultado = calcular(4, 2, '*')

print(resultado)
