# Sistema de Login com Tentativas Limitadas:
# Desenvolva um programa que simule um sistema de login.
# O programa deve solicitar o nome de usuário e senha até que o
# usuário insira as credenciais corretas ou até que o número máximo
# de tentativas seja atingido. Use um laço while com uma condicional
# para verificar as credenciais e limitar as tentativas.

login = 'Anderson'
senha = 1234
tentativas = 3

while tentativas > 0:
    login_acesso = input('Digite o nome de acesso: ')
    senha_acesso = int(input('Digite a senha de acesso: '))
    if login == login_acesso and senha == senha_acesso:
        print('Bem-vindo!')
        break
    else:
        print('Login e/ou senha errado, tente novamente!')
    tentativas -= 1
    print(f'Você tem {tentativas} tentativas!')

if tentativas == 0:
    for tentativas in range(3):
        print('Acesso bloqueado')