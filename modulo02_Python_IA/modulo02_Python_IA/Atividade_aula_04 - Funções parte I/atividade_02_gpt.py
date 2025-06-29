# 1. Par ou Ímpar com função
# Enunciado:
# Crie uma função chamada par_ou_impar(numero) que diga se o número é par ou ímpar.
# Use um while True para permitir que o usuário continue testando números até digitar -1.

def par_ou_impar (numero):
    if numero % 2 == 0:
        return f'O número {numero} é par'
    else:
        return f'O número {numero} é ímpar'
while True:
    numero = int(input('Digite um número ou -1 para sair: '))
    if numero == -1:
        break
    resposta = par_ou_impar(numero)
    print(f'Resposta: {resposta}')