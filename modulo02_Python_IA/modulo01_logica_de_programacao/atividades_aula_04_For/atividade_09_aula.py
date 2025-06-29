# Atividade 09:
# Verificar Números Pares e Impares com Interrupção:
# Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
# identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.

par = 0
impar = 0

for numero in range(1, 21):
    if numero == 15:
        print(f'O número é 15, o programa acabou! A quantidade de impares é {impar} e pares é {par}')
        break
    elif numero % 2 == 0:
        par += 1
    else:
        impar += 1