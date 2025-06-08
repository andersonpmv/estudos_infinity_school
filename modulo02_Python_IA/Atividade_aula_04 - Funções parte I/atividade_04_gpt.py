# ✅ 3. Calculadora simples
# Enunciado:
# Crie uma função calcular(a, b, operador) que faça:
# Soma se operador for "+"
# Subtração se for "-"
# Multiplicação se for "*"
# Divisão se for "/"

# Exemplo de uso:
# Editar
# calcular(10, 5, '+') → 15
# calcular(8, 2, '/') → 4

def calcular (a, b, operador):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        if b == 0:
            return 'O divisor não pode ser zero'
        return a / b
    else:
        return 'Não digitou um operador válido!'
    
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
operador = input('Digite o operador: ')

resultado = calcular (a, b, operador)
print(f'Resultado: {resultado}\n')


### CORREÇÃO GPT###

# ✅ O que está certo:
# Função calcular() trata os quatro operadores básicos ✔️

# Usa input() para receber os dois números e o operador ✔️

# Usa return para devolver o valor calculado ✔️

# Boa estrutura geral ✔️

# ⚠️ Pequeno detalhe a corrigir:
# Se o usuário digitar um operador inválido (ex: %), sua função retorna uma string de erro:

# return 'Não digitou um operador válido!'
# Mas no print, você tenta formatar como número:

# Editar
# print(f'Resultado: {resultado:.0f}')
# Isso vai causar erro se resultado for uma string.

