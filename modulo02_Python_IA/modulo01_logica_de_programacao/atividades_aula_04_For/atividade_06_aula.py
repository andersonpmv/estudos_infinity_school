# Atividade 06:
# Soma de Números Pares:
# Escreva um programa que use um laço for para somar
# todos os números pares de 1 a 50 e exiba o resultado final.

soma = 0
for numero in range(1,51):
    if numero % 2 == 0:
        soma += numero
print(soma)