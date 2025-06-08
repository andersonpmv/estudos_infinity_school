# ATIVIDADE PRÁTICA 2

# Crie um programa que define uma função
# calcular_area_retangulo que recebe dois argumentos,
# comprimento e largura de um retângulo, e retorna a
# área desse retângulo. Em seguida, o programa deve
# solicitar ao usuário que insira o comprimento e a
# largura e imprimir a área calculada.

def calcular_area_retangulo(comp, alt):
    area = comp * alt
    return area
comprimento = float(input('Digite o comprimento: '))
altura = float(input('Digite a altura: '))

print(f'A área é {calcular_area_retangulo(comprimento, altura):.2f}')