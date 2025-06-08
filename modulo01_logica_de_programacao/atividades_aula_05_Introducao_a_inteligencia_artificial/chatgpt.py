numero_alunos = int(input("Digite o número de alunos: "))
soma_medias = 0

for i in range(numero_alunos):
    print(f"\nAluno {i + 1}")
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    # Calcula a média do aluno
    media = (nota1 + nota2 + nota3) / 3
    soma_medias += media

    # Verifica se foi aprovado ou reprovado
    if media >= 7.0:
        status = "Aprovado ✅"
    else:
        status = "Reprovado ❌"

    # Exibe os dados do aluno
    print(f"\n--- Resultado ---")
    print(f"Nome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")

# Calcula e exibe a média geral da turma
media_geral = soma_medias / numero_alunos
print(f"\n📊 Média geral da turma: {media_geral:.2f}")