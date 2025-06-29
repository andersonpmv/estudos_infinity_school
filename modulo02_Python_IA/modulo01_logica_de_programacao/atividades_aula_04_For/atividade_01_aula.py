# Atividade 01:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).

numero = int(input('Digite um número: '))
for tabuada in range(1,11):
    print(f'{tabuada} x {numero} = {tabuada * numero}')