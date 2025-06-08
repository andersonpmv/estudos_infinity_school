# DESAFIO PRÁTICO

# Suponha que você está gerenciando uma competição esportiva e tem
# uma lista de tuplas representando os resultados das equipes em
# diferentes modalidades. Cada tupla contém o nome da equipe, seguido
# por uma lista de pontuações obtidas em cada rodada da competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a classificação final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a
# mais baixa.


lista_tupla = [
    ('nome equipe A', [10.00, 8.00, 9.00]),
    ('nome equipe B', [7.00, 9.00, 8.00]),
    ('nome equipe C', [10.00, 10.00, 10.00])
]

medias = [(lista_tupla[0][1][0] + lista_tupla[0][1][1] + lista_tupla[0][1][2]) / len(lista_tupla[0][1]),
          (lista_tupla[1][1][0] + lista_tupla[1][1][1] + lista_tupla[1][1][2]) / len(lista_tupla[1][1]),
          (lista_tupla[2][1][0] + lista_tupla[2][1][1] + lista_tupla[2][1][2]) / len(lista_tupla[2][1])
]


classificacao = [(lista_tupla[0][0], medias[0]), 
                 (lista_tupla[1][0], medias[1]),
                 (lista_tupla[2][0], medias[2])
]

classificacao.sort(key=lambda x: x[1], reverse=True)

print(classificacao)


# Resposta CHATGPT

# lista_tupla = [
#     ('nome equipe A', [10.00, 8.00, 9.00]),
#     ('nome equipe B', [7.00, 9.00, 8.00]),
#     ('nome equipe C', [10.00, 10.00, 10.00])
# ]

# medias = []
# for equipe in lista_tupla:
#     nome = equipe[0]
#     notas = equipe[1]
#     soma = notas[0] + notas[1] + notas[2]  # ainda fixo, mas você pode usar sum(notas)
#     media = soma / len(notas)
#     medias.append((nome, media))

# # Ordenação sem lambda
# for i in range(len(medias)):
#     for j in range(i + 1, len(medias)):
#         if medias[i][1] < medias[j][1]:
#             temp = medias[i]
#             medias[i] = medias[j]
#             medias[j] = temp

# # Exibir resultado
# for item in medias:
#     print(item[0], "média:", round(item[1], 2))