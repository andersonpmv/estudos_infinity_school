# Desenvolver um programa de linha de comando que permite
# aos usuários gerenciar suas tarefas diárias, atribuindo-lhes
# prioridades e categorias. O projeto será organizado em várias
# partes e usará funções, listas, tuplas, dicionários e conjuntos. Passos do projeto:

# Definição de Dados:

# Defina estruturas de dados para representar tarefas. Cada tarefa pode incluir

# informações como nome, descrição, prioridade e categoria. Você pode usar
# dicionários para representar as tarefas.

# Funções:
# Crie funções para adicionar tarefas, listar tarefas, marcar tarefas
# como concluídas, exibir tarefas por prioridade ou categoria, e outras
# funcionalidades que desejar.

# Menu de Comandos:
# Crie um menu de comandos de linha de comando que permita ao
# usuário interagir com o programa.

tarefas = []
def adicionar_tarefas():
    nome_tarefa = input('Nome da tarefa: ')
    descricao = input('\nDescrição da tarefa: ')
    prioridade = int(input('\nPrioridade da tarefa\n[1] Baixa\n[2] Média\n[3] Alta\nSelecione a opção: '))
    categoria = int(input('\nCategoria da tarefa\n[1] Lazer\n[2] Pessoal\n[3] Profissional\nSelecione a opção: '))
    status = int(input('\nStatus da tarefa\n[1] Concluída\n[2] Não concluída\nSelecione a opção: '))
    print()
    while prioridade < 1 or prioridade >3 or categoria < 1 or categoria > 3 or status < 1 or status > 2:
        if prioridade < 1 or prioridade > 3:
            prioridade = int(input('\nOpção inválida, escolha novamente!\n\nPrioridade da tarefa\n[1] Baixa\n[2] Média\n[Alta]\nSelecione a opção: '))
        if categoria < 1 or categoria > 3:
            categoria = int(input('\nOpção inválida, escolha novamente!\n\nCategoria da tarefa\n[1] Lazer\n[2] Pessoal\n[3] Profissional\nSelecione a opção: '))
        if status < 1 or status > 2:
            status = int(input('\nOpção inválida, escolha novamente!\n\nStatus da tarefa\n[1] Concluída\n[2] Não concluída\nSelecione a opção: '))
    
    if prioridade == 1:
        prioridade = 'Baixa'
    elif prioridade == 2:
        prioridade = 'Média'
    else:
        prioridade = 'Alta'

    if categoria == 1:
        categoria = 'Lazer'
    elif categoria == 2:
        categoria = 'Pessoal'
    else:
        categoria = 'Profissional'
    
    if status == 1:
        status = 'Concluído!'
    else:
        status = 'Não Concluído!'

    nova_tarefa = {'Nome': nome_tarefa,
                   'Descrição': descricao,
                   'Prioridade': prioridade,
                   'Categoria': categoria,
                   'Status': status
                   }
    tarefas.append(nova_tarefa)
    for i in range(len(tarefas)):
        print(f'Tarefa {i+1}')
        for chave, valor in tarefas[i].items():
            print(f'{chave}: {valor}')
        print()

def listar_tarefas():
    for i in range(len(tarefas)):
        print(f'Tarefa {i+1}')
        for chave, valor in tarefas[i].items():
            print(f'{chave}: {valor}')
        print()

def concluir_tarefa():
    while True:
        nome_tarefa = input('Qual tarefa deseja marcar como concluída: ')
        for i in range(len(tarefas)):
            if nome_tarefa in tarefas[i]['Nome']:
                tarefas[i]['Status'] = 'Concluído!'
                listar_tarefas()
                return       
        print('Tarefa não encontrada, digite o nome novamente!\n')

def prioridade_tarefa():
    while True:
        definir_prioridade = int(input('Qual prioridade deseja apresentar primeiro\n[1] Alta\n[2] Média\n[3] Baixa\nSelecione a opção: '))
        ordem_prioridade = {
            'Alta': 1,
            'Média': 2,
            'Baixa': 3
        }
        if definir_prioridade == 1:
            prioridade_ordem = sorted(tarefas, key= lambda tarefa: ordem_prioridade[tarefa['Prioridade']])

        elif definir_prioridade == 3:
            prioridade_ordem = sorted(tarefas, key= lambda tarefa: ordem_prioridade[tarefa['Prioridade']], reverse=True)
        
        elif definir_prioridade == 2:
            ordem_prioridade = {
            'Alta': 2,
            'Média': 1,
            'Baixa': 3
        }
            prioridade_ordem = sorted(tarefas, key= lambda tarefa: ordem_prioridade[tarefa['Prioridade']])
        else:
            print('Digitou uma opção inválidade, digite novamente!')
            continue
        break
    for i in range(len(prioridade_ordem)):
        print(f'Tarefa {i+1}')
        for chave, valor in prioridade_ordem[i].items():
            print(f'{chave}: {valor}')
        print()

def categoria_tarefa():
    while True:
        definir_categoria = int(input('Categorias\n[1] Lazer\n[2] Pessoal\n[3] Profissional\nEscolha a opção: '))
        ordem_categoria = {
            'Lazer': 1,
            'Pessoal': 2,
            'Profissional': 3
        }
        if definir_categoria == 3:
            categoria_ordem = sorted(tarefas, key= lambda tarefa: ordem_categoria[tarefa['Categoria']], reverse=True)
        elif definir_categoria == 1:
            categoria_ordem = sorted(tarefas, key= lambda tarefa: ordem_categoria[tarefa['Categoria']])
        elif definir_categoria == 2:
            ordem_categoria = {
                'Lazer': 2,
                'Pessoal': 1,
                'Profissional': 3
            }
            categoria_ordem = sorted(tarefas, key= lambda tarefa: ordem_categoria[tarefa['Categoria']])
        else:
            print('Opção errada, digite novamente!')
            continue
        break
    for i in range(len(categoria_ordem)):
        print(f'Tarefa {i+1}')
        for chave, valor in categoria_ordem[i].items():
            print(f'{chave}: {valor}')
        print()

while True:
    menu = int(input(f'Menu - Escolha uma opção:\n\n[1] Listar tarefas\n[2] Adicionar tarefa\n[3] Concluir tarefa\n[4] Por prioridade\n[5] Por categoria\n[6] Sair do programa\n\nSelecione a opção: '))
    print()
    if menu == 1:
        if not tarefas:
            print('A sua lista de tarefas ainda esta vazia!!!\n')
        else:
            listar_tarefas()
    elif menu == 2:
        adicionar_tarefas()
    elif menu == 3:
        concluir_tarefa()
    elif menu == 4:
        prioridade_tarefa()
    elif menu == 5:
        categoria_tarefa()
    elif menu == 6:
        print('Até mais!')
        break
    else:
        print('Digitou uma opção invalida, digite de novo!')