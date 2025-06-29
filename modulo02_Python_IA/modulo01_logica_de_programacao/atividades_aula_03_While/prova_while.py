# Você está criando um programa em Python para simular um jogo simples de adivinhação. 
# O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
# O jogador terá até 3 tentativas para acertar o número.
# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas 
# tentativas até acertar ou atingir o limite de tentativas. 
# Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte 
# e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

numero = 7
tentativas = 3
while tentativas >= 1:
    adivinhe = int(input('Digite um número: '))
    if adivinhe == 7:
        print(f'Parabéns, você acertou! O número era {adivinhe}!!!')
        break
    else:
        tentativas -= 1
        print (f'Você tem mais {tentativas} tentativas!')
else:
    print('Que pena, você perdeu! tente de novo!')