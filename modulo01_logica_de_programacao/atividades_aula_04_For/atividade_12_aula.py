# Atividade 12:
# Soma de Números com Desconto:
# Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
# calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
# interrompa o loop com break.

soma = 0
for cont in range(1, 6):
    valor = float(input('Digite o preço: '))
    soma += valor
    if cont == 5:
        if soma > 100:
            print(f'O valor é {soma:.2f}, ganhou desconto de 10%! O valor total será de {soma - soma * 0.1:.2f}')
        else:
            print(f'O valor é de {soma:.2f}')
        break