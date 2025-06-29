# ATIVIDADE PRÁTICA 6

# Crie um programa que recebe dois conjuntos e exibe a interseção deles.

a = set(input('Digite o conjunto separado por virgula: ').split(','))
b = set(input('Digite o outro conjunto separado por virgula: ').split(','))

print(a & b)