# Você está desenvolvendo um programa em Python para calcular a soma dos 
# números pares dentro de um intervalo determinado pelo usuário. 
# O programa deve solicitar ao usuário que insira dois números inteiros, 
# representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. 
# Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, 
# caso seja o caso.

# Ao final, exiba a soma dos números pares encontrados.


soma = 0
while True:
    numero1 = int(input('Digíte um número de inicio: '))
    numero2 = int(input('Digíte um número de término: '))
    if numero1 > numero2:
        print('O número de inicio é maior que o de término, digite novamante!')
        continue
    else:
        for i in range(numero1, numero2):
            if i % 2 == 0:
                soma += i
                print(i, soma)
    break
print (f'A soma dos número pares é de {soma}')