# ATIVIDADE PRÁTICA 2

# Crie um módulo chamado manipulacao_strings que
# contenha funções para realizar operações com strings,
# como inverter uma string, contar o número de palavras

# em uma string e verificar se uma string é um
# palíndromo (lê-se igual de trás para frente). Crie
# um programa principal que importe o módulo e use
# essas funções com strings fornecidas pelo usuário.

def manipulacao(operacao, texto):
    if operacao == 1:
        palavra_invertida = texto[::-1]
        return f'A palavra invertida: {palavra_invertida}'
    elif operacao == 2:
        total_palavras = len(texto.split())
        return f'O total de palavras é: {total_palavras}'
    elif operacao == 3:
        palavra_invertida = texto[::-1]
        if palavra_invertida == texto:
            return f'A palavra {texto} é um palíndromo!'
        else:
            return f'A palavra {texto} não é um palíndromo!'
    else:
        return 'Operação inválida, escolha novamente!'