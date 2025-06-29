# ATIVIDADE PRÁTICA 4

# Desenvolva um jogo de adivinhação em que o programa
# escolhe um número aleatório e desafia o jogador a
# adivinhá-lo. Forneça dicas ao jogador, indicando se o
# número é maior ou menor do que a adivinhação atual.

import random

def continuar_jogo():
    while True:
        continuar = int(input('Deseja continuar?\n'
                              '[1] Sim\n'
                              '[2] Não\n' \
                              'Escolha a opção: '))
        if continuar == 1:
            return True
        elif continuar == 2:
            print('\nAté a próxima!')
            return False
        else:
            print('Opção inválida, tente novamente!\n')

def jogo_adivinhacao(start):
    if start == 2:
        print('\nAté a próxima!')
        return 2

    numero_adivinhar = random.randint(1, 10)

    while True:
        numero = int(input('\nEscolha um número de 1 a 10: '))
        print()
        
        if numero > numero_adivinhar and numero <= 10:
            print('Boa tentativa, mas o número é menor!\n')
        elif numero < numero_adivinhar and numero >= 1:
            print('Boa tentativa, mas o número é maior!\n')
        elif numero < 1 or numero > 10:
            print('Número inválido, tente novamente!\n')
            continue
        else:
            print(f'Acertou! O número é {numero_adivinhar}\n')
            print('VAMOS JOGAR DE NOVO?\n')
            continuar = continuar_jogo()
            if continuar == True:
                break
            else:
                return 2

        if continuar_jogo() == False:
            return 2

    return 1