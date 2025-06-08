# Atividade 11:
# Verificar Múltiplos de 5 e Parar:
# Escreva um programa que use um laço for para imprimir números de 1 a 30.
# Use uma condicional para verificar se um número é múltiplo de 5 e outro
# para verificar se é maior que 20 e interromper o loop com break.

soma = 0
for cont in range (1,31):
    print (cont)
    if cont > 20:
        print (f'O progrmada acabou! Possuí {soma} multiplos de 5')
        break
    elif cont % 5 == 0:
        soma += 1