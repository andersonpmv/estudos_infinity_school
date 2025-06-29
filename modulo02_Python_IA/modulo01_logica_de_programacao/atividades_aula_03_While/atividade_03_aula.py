# Atividade 03:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).

tabuada = int(input('Digite um numero: '))
contador = 1

while contador < 11:
    print(f'{tabuada} x {contador} = {tabuada * contador}')
    contador += 1
print('-' * 20)

# Outra forma de fazer
contador = 1
while contador < 11:
    resultado = tabuada * contador
    print(f'{tabuada} x {contador} = {resultado}')
    contador += 1
