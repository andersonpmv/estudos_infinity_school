# DESAFIO PRÁTICO

# Sistema de Cadastro de Alunos

# Cadastro de Alunos: O programa deve permitir ao usuário cadastrar alunos. Cada aluno terá as seguintes
# informações: nome, idade e notas em três disciplinas:
# Matemática, Ciências e História. Os dados de cada aluno devem ser armazenados em um dicionário com as
# seguintes chaves: 'nome', 'idade', 'notas'. As notas devem ser armazenadas em uma tupla.

# Visualização de Alunos: O programa deve permitir ao usuário
# visualizar todos os alunos cadastrados, exibindo suas informações de forma organizada.
# Média de Notas: O programa deve calcular a média das notas de cada aluno e exibi-la.
# Aluno com Melhor Média: O programa deve identificar e
# exibir o aluno com a melhor média de notas.

alunos = []

while True:
    cadastrar = input('Deseja cadastrar um aluno? "s"sim e "n" não: ').lower()
    if cadastrar == 'n':
        break
    dicio = {}
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade: '))
    nota01 = float(input('Digite a nota de matemática: '))
    nota02 = float(input('Digite a nota de ciência: '))
    nota03 = float(input('Digite a nota de história: '))
    dicio ['Nome'] = nome
    dicio ['Idade'] = idade
    dicio ['Notas'] = (nota01, nota02, nota03)
    alunos.append(dicio)
medias = {}
for cada_aluno in alunos:
    for chave, valor in cada_aluno.items():
        print(f'{chave}: {valor}')
        if chave == 'Notas':
            media = sum(valor) / len(valor)
            medias[cada_aluno['Nome']] = media
            print(f'A média das notas é: {media:.2f} \n\n')
            

medias = dict(sorted(medias.items(), key=lambda item: item[1], reverse=True))
for chave, valor in medias.items():
    print(f'A maior média foi do aluno(a) {chave} e a média foi {valor:.2f}\n\n')
    break