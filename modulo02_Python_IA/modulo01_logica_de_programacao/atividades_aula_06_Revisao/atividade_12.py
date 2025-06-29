# Sistema de Login:
# Desenvolva um programa que simule um sistema de login.
# O programa deve pedir o nome de usuário e a senha e verificar
# se correspondem a um usuário pré-cadastrado. Exiba mensagens
# apropriadas para login bem-sucedido ou falha.

login = 'Anderson'
senha = 1234

while True:
    login_acesso = input('Digite o nome de acesso: ')
    senha_acesso = int(input('Digite a senha de acesso: '))
    if login == login_acesso and senha == senha_acesso:
        print('Acesso bem-sucedido')
        break
    else:
        print('Login e/ou senha errado, tente novamente!')