# ✅ 2. Média de 3 números
# Enunciado:
# Crie uma função chamada media(a, b, c) que receba três números e retorne a média.
# Peça os números ao usuário e mostre a média.
def media (a, b, c):
    return (a + b + c) / 3
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

media_resp = media(a, b, c)

print(f'A media é {media_resp:.2f}')