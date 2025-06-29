import at02_1_manipulacao_strings

while True:
    operacao = int(input('Manipulando Strings\n' \
                         '[1] Inverter o texto\n' \
                         '[2] Contar as palavaras\n' \
                         '[3] Verificar se é um palíndromo\n' \
                         '[4] Sair\n\n'
                         'Selecione a Opção: '))
    if operacao == 4:
        print('Até mais!')
        break
    texto = input('Digite uma palavra ou um texto: ')

    resposta = at02_1_manipulacao_strings.manipulacao(operacao, texto)
    print(f'\n{resposta}\n')