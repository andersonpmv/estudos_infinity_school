# Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.

segundos = int(input('Digite a quantidade de segundos: '))
seg = segundos
horas = 0
minutos = 0

while segundos >= 60:
    while segundos >= 3600:
        horas += 1
        segundos -= 3600
    if segundos < 3600 and segundos >= 60:
        minutos += 1
        segundos -= 60

print (f'{horas}:{minutos}:{segundos}')

# Resposta ChatGPT
print(40 * '-')

horas = seg // 3600
minutos = (seg % 3600) // 60
segundos = (seg % 3600) % 60

print (f'{horas}:{minutos}:{segundos}')