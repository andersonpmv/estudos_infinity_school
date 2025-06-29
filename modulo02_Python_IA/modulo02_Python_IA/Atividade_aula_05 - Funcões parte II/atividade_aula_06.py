# ATIVIDADE PRÁTICA 6

# Crie uma função que aceita uma lista de strings e use a
# função reduce (importada de functools) para encontrar
# a maior string na lista.

from functools import reduce
nomes = ['and', 'ander', 'anders', 'anderson']
maior = reduce(lambda x, y: x if len(x) > len(y) else y, nomes)

print(maior)