# Atividade 08:
# Cálculo de Média de Notas:
# Escreva um programa que solicite 5 notas de alunos. Use um laço for
# para somar as notas e uma condicional para exibir a média e a
# classificação ("Aprovado" para média >= 6,
# "Reprovado" para média < 6).

soma = 0
for numero in range(1,6):
    nota = float(input('Digite a nota: '))
    soma += nota
    if numero == 5:
        media = soma / numero
        if media >= 6:
            print(f'A média é {media}, o aluno esta APROVADO!')
        else:
            print(f'A média é {media}, o aluno esta REPROVADO!')