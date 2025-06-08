# ATIVIDADE PRÁTICA 13

# Crie um dicionário que relacione nomes de alunos às suas
# notas em uma disciplina. Calcule a média das notas e exiba-a.

alunos = {
    'A':[7,8,9],
    'B':[4,5,6],
    'C':[10,9,10]
}

for chave, valor in alunos.items():
    media = sum(valor)/len(valor)
    print(f'O aluno {chave}, tirou a média {media:.2f}')

