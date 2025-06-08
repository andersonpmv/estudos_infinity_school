# Atividade 07:
# Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.

numero = int(input('Digite um numero: '))
multiplicar = 1
tabuada = 0
while multiplicar < 11:
    tabuada = multiplicar * numero
    if tabuada % 3 == 0:
        print(f'O numero {tabuada} é multiplo de 3!')
    multiplicar += 1