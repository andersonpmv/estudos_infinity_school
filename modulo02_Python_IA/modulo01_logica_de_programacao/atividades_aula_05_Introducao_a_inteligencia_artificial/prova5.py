# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. 
# O programa deve solicitar ao usuário o número de alunos e, 
# em seguida, para cada aluno, pedir o nome e três notas. 
# Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, 
# considerando que a média mínima para aprovação é 7.0. 
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.

# Refazendo a questão

qauntidade_alunos = int(input('Digite a quantidade de alunos: '))
media_geral = 0
for i in range(qauntidade_alunos):
    aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    media = (nota1 + nota2 + nota3) / 3
    media_geral += media
    if media >= 7:
        print(f'O Aluno {aluno} tirou as notas {nota1}, {nota2}, e {nota3} \nSua média foi de {media}\nAprovado!')
    else:
        print(f'O Aluno {aluno} tirou as notas {nota1}, {nota2}, e {nota3} \nSua média foi de {media}\nReprovado!')
        
print(f'A média geral da turma é de {media_geral/qauntidade_alunos}')