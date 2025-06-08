# Crie uma função chamada dobro_ou_triplo(numero) que:
# Retorna o dobro do número se ele for par
# Retorna o triplo se for ímpar
# Quer que eu corrija depois que você fizer? Posso ajudar!

def dobro_ou_triplo(numero):
    if numero % 2 == 0:
        return numero * 2
    else:
        return numero * 3
while True:
    numero = int(input('Digite um número ou -1 para sair: '))
    if numero == -1:
        break
    resultado = dobro_ou_triplo(numero)
    print(f'Resultado: {resultado}')
