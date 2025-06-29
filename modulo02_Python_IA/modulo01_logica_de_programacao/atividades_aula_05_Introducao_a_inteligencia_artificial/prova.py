# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. 
# O programa deve solicitar ao usuário o número de alunos e, 
# em seguida, para cada aluno, pedir o nome e três notas. 
# Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, 
# considerando que a média mínima para aprovação é 7.0. 
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.


nomes_alunos = []
notas = []
medias = []
soma_medias = 0
quantidade_alunos = int(input('Digíte a quantide de alunos: '))
for cont_aluno in range(1, quantidade_alunos + 1):
    aluno = input (f'Digíte o nome do aluno {cont_aluno}: ')
    nomes_alunos.append(aluno)
    nota1 = float(input(f'Digite a primeira nota do aluno(a) {aluno}: '))
    nota2 = float(input(f'Digite a segunda nota do aluno(a) {aluno}: '))
    nota3 = float(input(f'Digite a terceira nota do aluno(a) {aluno}: '))
    notas.append([nota1, nota2, nota3])
    media = (nota1 + nota2 + nota3) / 3
    medias.append(media)
    soma_medias += media

for cont_aluno in range(quantidade_alunos):
    nota1, nota2, nota3 = notas[cont_aluno]
    media = medias[cont_aluno]
    nome = nomes_alunos[cont_aluno]
    print(f'''O aluno(a) {nome} tirou as notas: 
{nota1}, {nota2} e {nota3} 
A sua média final foi de {media:.2f}''')
    if medias[cont_aluno] >= 7:
        print('Aprovado!\n\n')
    else:
        print('Reprovado\n\n')

print(f'A média geral da turma foi de {soma_medias/quantidade_alunos:.2f}')