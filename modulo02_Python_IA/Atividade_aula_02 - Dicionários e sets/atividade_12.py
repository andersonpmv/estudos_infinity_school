# ATIVIDADE PRÁTICA 12

# Crie um programa que simule um sistema de votação. O
# programa deve permitir que os eleitores escolham entre
# opções de eleitores e conte os votos para cada opção.
# Use um dicionário para armazenar os resultados da
# votação, onde as chaves são as opções e os valores são o
# número de votos para cada opção. O programa deve
# permitir que os eleitores votem, encerre a votação e exiba
# os resultados finais. Use While True e pare o programa
# somente se o usuário digitar o número 0 e exiba os resultados finais.

cont_a = 0
cont_b = 0
cont_c = 0

dicio = {
    'Candidato A': cont_a,
    'Candidato B': cont_b,
    'Candidato C': cont_c
}

while True:
    candidato = input('Digite o nome do candidato a, b ou c: ').lower()
    voto = input ('Confirma o voto, "s" sim e "n" não: ').lower()
    if voto == 's':
        if candidato == 'a':
            cont_a += 1
            dicio['Candidato A'] = cont_a
        elif candidato == 'b':
            cont_b += 1
            dicio['Candidato B'] = cont_b
        else:
            cont_c += 1
            dicio['Candidato C'] = cont_c
    else:
        continue
    continuar = input('Deseja sair? digite "0": ')
    if continuar == '0':
        break
print(dicio)
