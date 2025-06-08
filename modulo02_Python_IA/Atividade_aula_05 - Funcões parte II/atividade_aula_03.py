# ATIVIDADE PRÁTICA 3

# Crie uma função chamada concatenar_strings que
# aceita um número variável de strings como argumentos
# posicionais (usando *args). A função deve concatenar
# todas as strings em uma única string e retorná-la.

def concatenar_strings(*strings):
    palavra = ''.join(strings)
    return palavra

print(concatenar_strings('a','n','d','e','r','s','o','n'))