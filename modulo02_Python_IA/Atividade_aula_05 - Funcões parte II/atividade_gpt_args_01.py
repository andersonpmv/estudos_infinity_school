
def somar(*args):
    resultado = 0
    for numero in range (len(args)+1):
        resultado += numero
    return resultado


print(somar(1, 2, 3, 4))