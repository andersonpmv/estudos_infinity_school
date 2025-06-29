# ATIVIDADE PRÁTICA 3

# Crie um programa que permite ao usuário calcular a
# área e operímetro de formas geométricas simples,
# como quadrados, retângulos e círculos. Use funções
# matemáticas do módulo math para realizar os cálculos.

import math

def quadrado(num1):
    area = num1 * num1
    perimetro = num1 * 4
    return f'Quadrado\nÁrea: {area} | Perímetro {perimetro}'

def retangulo(num1, num2):
    area = num1 * num2
    perimetro = (num1 + num2) *2
    return f'Retângulo\nÁrea: {area} | Perímetro {perimetro}'


def circulo(num1):
    area = math.pi * math.pow(num1, 2)
    perimetro = 2 * math.pi * num1
    return f'Circulo\nÁrea: {area:.2f} | Circunferência {perimetro:.2f}'