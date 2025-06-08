# Atividade 10:
# Soma até 50:
# Escreva um programa que use um laço while para somar
# números consecutivos começando de 1 e termine quando
# a soma atingir ou ultrapassar 50.

numero = 1
soma = 0
while True:
    soma += numero
    print (numero, soma)
    numero += 1
    if soma >= 50:
        break
    