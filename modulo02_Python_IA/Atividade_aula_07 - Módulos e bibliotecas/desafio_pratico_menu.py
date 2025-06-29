import desafio_pratico

while True:
    menu = int(input('GERENCIADOR DE LIVROS\n' \
                     '[1] Exibir os livros\n' \
                     '[2] Adicionar um livro\n' \
                     '[3] Livros disponíveis\n' \
                     '[4] Emprestar livro\n' \
                     '[5] Devolver livro\n' \
                     '[6] Consultar livro disponível\n'
                     '[7] Listar emprestimos\n' \
                     '[8] Sair\n\n' \
                     'Escolha uma opção: '))
    print()
    if menu == 8:
        break
    elif menu == 1:
        desafio_pratico.listar_livros()
    elif menu == 2:
        desafio_pratico.adicionar_livro()
    elif menu == 3:
        desafio_pratico.livros_disponiveis()
    elif menu == 4:
        desafio_pratico.emprestar_livros()
    elif menu == 5:
        desafio_pratico.devolver_livro()
    elif menu == 6:
        desafio_pratico.disponibilidade_livro()
    elif menu == 7:
        desafio_pratico.listar_emprestimos()
    else:
        print('Opção inválida, escolha de novo!')