# Atividade 10:
# Contar Números Positivos e Negativos:
# Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
# são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.

positivo = 0
negativo = 0

for cont in range(1,11):
    numero = int(input('Digite um numero nagativo ou positivo: '))
    if numero == 0:
        print(f'Digitou 0, o programa acabou! Digitou {negativo} números nagativos e {positivo} numeros positivos!')
        break
    elif numero > 0:
        positivo += 1
    elif numero < 0:
        negativo +=1
    if cont == 10:
        print (f'Digitou {positivo} positivos e {negativo} negativos!')