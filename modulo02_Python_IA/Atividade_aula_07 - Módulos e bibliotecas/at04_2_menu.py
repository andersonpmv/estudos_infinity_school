import at04_1_jogo_adivinhacao

jogar = int(input('VAMOS JOGAR?\n' \
                  '[1] Sim\n' \
                  '[2] Não\n'
                  'Escolha uma opção: '))

while True:
    jogar = at04_1_jogo_adivinhacao.jogo_adivinhacao(jogar)
    if jogar == 2:
        break  