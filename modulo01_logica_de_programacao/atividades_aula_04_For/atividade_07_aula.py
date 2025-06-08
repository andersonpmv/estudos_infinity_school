# Atividade 07:
# Contagem de Vogais em uma Palavra:
# Crie um programa que solicite uma palavra ao usuário e use um laço for com
# uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.

palavra = input('Digite uma palavra: ')
soma = 0
for letra in palavra:
    if letra.lower() in 'aeiou':
        soma += 1
print (f'A palavra possuí {soma} vogais!')