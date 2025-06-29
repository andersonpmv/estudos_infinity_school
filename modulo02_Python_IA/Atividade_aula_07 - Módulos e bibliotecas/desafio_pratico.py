# DESAFIO PRÁTICO

# Gerenciador de Livros de Biblioteca

# Crie um programa que permita aos usuários:
# Adicionar novos livros à biblioteca, com informações como título,
# autor e número de cópias disponíveis.
# Listar todos os livros disponíveis na biblioteca.
# Permitir aos usuários fazer empréstimos de livros, reduzindo o
# número de cópias disponíveis quando um livro é emprestado.
# Permitir aos usuários devolver livros, aumentando o número de
# cópias disponíveis quando um livro é devolvido.
# Verificar a disponibilidade de um livro específico na biblioteca.

lista_de_livros = []
lista_emprestados = []

def exibir(exemplar):
    for chave, valor in exemplar.items():
        print(f'{chave}: {valor}')

def listar_livros():
    for exemplar in lista_de_livros:
        exibir(exemplar)
        print()
    print()

def adicionar_livro():
    titulo = input('Título do livro: ').strip().capitalize()
    autor = input('Nome do autor: ').strip().capitalize()
    quantidade = int(input('Quantidade de livros: '))

    novo_livro = {
        'Titulo': titulo,
        'Autor': autor,
        'Quantidade': quantidade,
        'Disponíveis': quantidade,
        'Emprestados': 0
    }
    lista_de_livros.append(novo_livro)
    print('Livro adicionado!')

def livros_disponiveis ():
    encontrar = False
    for exemplar in lista_de_livros:
        if exemplar['Disponíveis'] > 0:
            exibir(exemplar)
            print()
            encontrar = True
    if not encontrar:
        print('Não tem livros disponíveis no momento!\n')

def emprestar_livros():
    livro = input('Qual livro deseja alugar: ').strip().capitalize()
    encontrar = False # flag (variável de controle) para veficar se encontra o livro.
    for exemplar in lista_de_livros:
        if livro == exemplar['Titulo']:
            encontrar = True
            if exemplar['Disponíveis'] > 0:
                nome = input('Qual é o seu nome: ').strip().capitalize()
                emprestar = {
                    'Nome': nome,
                    'Livro': livro
                }
                lista_emprestados.append(emprestar)
                exemplar['Disponíveis'] -= 1
                exemplar['Emprestados'] += 1
                print('Livro emprestado!\n')
            else:
                print('Esse livro não esta disponível no momento!')
            break   
    if not encontrar:
        print('Livro não encontrado!\n')


def devolver_livro():
    livro = input('Qual livro vai devolver: ').strip().capitalize()
    encontrar = False
    for exemplar in lista_de_livros:
        if livro == exemplar['Titulo']:
            encontrar = True
            nome = input('Qual é o seu nome: ')
            for item in lista_emprestados:
                if nome == item['Nome'] and livro == item['Livro']:
                    lista_emprestados.remove(item)
                    exemplar['Disponíveis'] += 1
                    exemplar['Emprestados'] -= 1
                    print('Livro devolvido!\n')
                    break
            else: 
                print('Nome ou livro não encontrado!\n')
            break
    if not encontrar:
        print('Livro não econtrado!\n')

def disponibilidade_livro():
    livro = input('Nome do livro: ').strip().capitalize()
    encontrar = False
    for exemplar in lista_de_livros:
        if livro == exemplar['Titulo']:
            encontrar = True
            if exemplar['Disponíveis'] > 0:
                print(f'{exemplar["Titulo"]}: Possui {exemplar["Disponíveis"]} livros disponíveis')
            else:
                print('Não possuí livros disponíveis\n')
    if not encontrar:
        print('Livro não encontrado!')

def listar_emprestimos():
    for item in lista_emprestados:
        for chave, valor in item.items():
            print(f'{chave}: {valor}')
        print()