# ATIVIDADE PRÁTICA 4

# Crie uma função que aceita uma lista de números e use
# a função map para retornar uma nova lista contendo o
# dobro de cada número na lista de entrada.

numeros = [1, 2, 3, 4, 5]

dobro = list(map(lambda x: x * 2, numeros))

print(dobro)