# ATIVIDADE PRÁTICA 2

# Crie uma função que receba um horário e imprima
# "Bom dia!", "Boa tarde!" ou "Boa noite!" conforme o horário.

def periodo(hora):
    if hora >= 0 and hora < 12:
        return 'Bom dia!'
    elif hora < 18:
        return 'Boa tarde!'
    elif hora <= 23:
        return 'Boa noite!'
    else:
        return 'Digitou um número inválido'    

hora = int(input('Digite o horário (sem os minutos!) de 0 a 23: '))

saudacao = periodo(hora)

print(saudacao)