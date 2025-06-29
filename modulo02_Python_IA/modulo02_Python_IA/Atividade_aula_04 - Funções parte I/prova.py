# [PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. 
# Esta função deve calcular a média aritmética desses três números. 
# Para fazer isso, some os três números e, em seguida, divida o resultado por três. 
# Por fim, a função deve retornar o valor da média aritmética calculada

def media(a, b, c):
    resposta = (a + b + c) / 3
    return resposta

print(f'{media(10, 5, 25):.2f}')
