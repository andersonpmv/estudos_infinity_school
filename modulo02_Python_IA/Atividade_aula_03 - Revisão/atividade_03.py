#Faça um programa que peça 10 números inteiros,
#calcule e mostre a quantidade de números pares e a
#quantidade de números impares.

impar = 0
par = 0

for i in range(10):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Possuí {par} pares e {impar} impares')
