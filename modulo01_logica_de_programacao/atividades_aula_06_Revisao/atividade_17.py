# Verificação de Palíndromo:
# Escreva um programa que solicite uma palavra ao usuário e
# use um laço while para verificar se a palavra é um palíndromo
# (lê-se da mesma forma de trás para frente).

palavra_inversa = ''
palavra = input('Digite uma palavra: ')
quantidade_letras = len(palavra)
while quantidade_letras > 0:
    quantidade_letras -= 1
    palavra_inversa += palavra[quantidade_letras]

if palavra == palavra_inversa:
    print(f'A palavra {palavra} é um palíndromo')
else:
    print(f'A palavra {palavra} não é um palíndromo')