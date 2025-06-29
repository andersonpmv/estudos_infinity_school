# DESAFIO PRÁTICO

# Calculadora

# Crie uma calculadora com opções de soma, multiplicação,
# subtração, divisão e sair.
# (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)
# Utilize funções de rotina para cada operação e funções de unidade lógica para
# realizar os cálculos.
# Dica:
# Utilize de condicionais e Laços de Repetição para realizar esse exercício.

def calculadora (a, b, calcular):
    if calcular == 1:
        return a + b
    elif calcular == 2:
        return a - b
    elif calcular == 3:
        return a * b
    elif calcular == 4:
        return a / b
def validar(opcao):
    if opcao in [1, 2, 3, 4]:
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo valor: '))
        if opcao == 4 and b == 0:
            return print('Divisão:\nDivisor não pode ser 0, escolha a opção de novo!\n\n')
        return calculadora(a, b, opcao)
    else:
        return print('Opção inválida, digite novamente!\n\n')
    
while True:
    entrada = int(input('Escolha uma opção:\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Sair\nQual opção deseja: '))
    if entrada == 5:
        print('Até mais!')
        break
    else:
        resposta = validar(entrada)
        if resposta == None:
            continue
        print(f'\n{resposta:.2f}\n')