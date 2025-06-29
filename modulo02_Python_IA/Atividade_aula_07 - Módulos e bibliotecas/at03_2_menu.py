import at03_1_modulo_math

while True:
    menu = int(input('Calcular formas geométricas\n' \
                         '[1] Quadrado\n' \
                         '[2] Retângulo\n' \
                         '[3] Círculo\n' \
                         '[4] Sair\n\n'
                         'Selecione a Opção: '))
    if menu == 4:
        print('Até mais!')
        break
    elif menu == 1:
        lado = int(input('Lado quadrado: '))
        resposta = at03_1_modulo_math.quadrado(lado)
        print (f'\n{resposta}\n')
    elif menu == 2:
        lado = int(input('Lado retângulo: '))
        base = int(input('Base retângulo: '))
        resposta = at03_1_modulo_math.retangulo(lado, base)
        print(f'\n{resposta}\n')
    elif menu == 3:
        raio = int(input('Raio circulo: '))
        resposta = at03_1_modulo_math.circulo(raio)
        print(f'\n{resposta}\n')
    else:
        print('Opção inválida, selecione a opção novamente!')