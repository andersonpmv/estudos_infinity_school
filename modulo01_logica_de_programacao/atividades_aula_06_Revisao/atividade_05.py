# Verificando a Média do Aluno:
# Crie um algoritmo que peça quatro notas de um aluno, calcule a
# média e exiba se o aluno foi aprovado ou reprovado (média >= 6).

soma = 0
for contagem in range (1,5):
    nota = float(input(f'Digite a nota {contagem}: '))
    soma += nota
media = soma / contagem
if media >= 6:
    print(f'A media é {media}, aluno aprovado!')
else:
    print(f'A media é {media}, aluno reprovado!')