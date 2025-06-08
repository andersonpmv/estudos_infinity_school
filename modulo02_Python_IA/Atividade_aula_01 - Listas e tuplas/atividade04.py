# Crie uma tupla para representar as informações de três
# palestrantes, cada uma contendo o nome, o tema da
# palestra e a instituição à qual estão vinculados.

# Exiba na tela as informações do terceiro palestrante,
# incluindo nome, tema da palestra e instituição.

palestrantes = (
    ('nome1', 'tema1', 'instituição1'),
    ('nome2', 'tema2', 'instituição2'),
    ('nome3', 'tema3', 'instituição3')
)

print(f'Palestrante: {palestrantes[2][0]}, tema: {palestrantes[2][1]}, instituição: {palestrantes[2][2]}')