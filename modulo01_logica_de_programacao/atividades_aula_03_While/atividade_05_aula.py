# Atividade 05:
# Contagem até o Número Inserido:
# Crie um programa que solicite um número ao usuário e use
# um laço while para contar de 1 até o número inserido,
# exibindo apenas os números ímpares.

numero = int(input('Digite um numero: '))
contador = 0

while contador <= numero:
    if contador % 2 == 1:
        print(contador)
        contador += 1
    else:
        contador += 1
