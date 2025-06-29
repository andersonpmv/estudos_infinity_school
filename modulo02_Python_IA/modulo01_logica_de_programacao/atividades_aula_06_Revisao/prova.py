# Crie um programa em Python que simule um sistema de login. 
# O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
# Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. 
# Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.

# Se todas as três tentativas falharem, 
# o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

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