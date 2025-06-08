lista = []
while True:
    entrada = input('Digite um elemento ou "s" para sair: ')
    if entrada == 's':
        break
    lista.append(entrada)
print(lista)

dicionario = {item: lista.count(item) for item in set(lista)}

print(dicionario)

print(2 * 3 + 1)