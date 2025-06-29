# [PYIA-A02] Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. 
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, 
# o número de telefone e o endereço de email. 
# Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, 
# mostrando todas as informações do contato inserido pelo usuário.

contatos = []
while True:
    continuar = input('Deseja infomar um contato, "s" para sim e "n" para não: ').lower()
    if continuar == 'n':
        break
    elif continuar != 's':
        print('Digitou errado, digite novamente!')
        continue
    nome = input('Digite o nome do contato: ')
    email = input('Digite o e-mail: ')
    telefone = input('Digite o número do telefone: ')
    
    contato = {
        'Nome': nome,
        'E-mail': email,
        'Telefone': telefone
    }
    contatos.append(contato)

for contato in contatos:
    for chave, valor in contato.items():
        print(f'{chave}: {valor}')
    print()