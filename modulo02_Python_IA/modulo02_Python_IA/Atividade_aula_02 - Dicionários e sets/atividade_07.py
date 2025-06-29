# ATIVIDADE PRÁTICA 7

# Escreva um programa que receba duas listas e calcule
# a união dos elementos únicos dessas listas, usando conjuntos.

a = set(input('Digite o conjunto separado por virgula: ').split(','))
b = set(input('Digite o outro conjunto separado por virgula: ').split(','))

print(a | b)