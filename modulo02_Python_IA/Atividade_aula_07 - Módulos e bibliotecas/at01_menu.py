import at01_calculadora

while True:
    operacao = int(input('Qual operação deseja realizar?\n[1] Somar\n[2] Subtrair\n[3] Dividir\n[4] Multiplicar\n[5] Sair\n\nEscolha a opção: '))
    if operacao == 5:
        print('Até mais!')
        break
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    resultado = at01_calculadora.calculadora(num1, num2, operacao)
    print(f'\nO resultado da operação é: {resultado}\n')