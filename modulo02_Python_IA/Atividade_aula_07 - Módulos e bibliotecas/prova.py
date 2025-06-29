import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    soma_dados = dado1 + dado2
    return soma_dados
print(f'A soma dos dados é {lancar_dados()}')