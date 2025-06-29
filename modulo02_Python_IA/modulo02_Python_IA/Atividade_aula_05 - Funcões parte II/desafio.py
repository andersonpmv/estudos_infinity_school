def processador_texto(texto, **kwargs):
    if kwargs.get('contar_palavras'):
        num_palavras = len(texto.split())
        print(f'Total de palvras: {num_palavras}')

    if kwargs.get('contar_letras'):
        num_letras = len(texto.replace())
        print(f'Total de palvras: {num_letras}')

    if kwargs.get('inverter_palavra'):
        reverter_palavra = texto[::-1]
        print(f'A palavra invertida fica: {reverter_palavra}')

    if kwargs.get('substituir palavra'):
        palavras_sep = texto.split()
        palavra_substituir = input(f'Qual palavra deseja substituir da frase {texto}: ')
        nova_palavra = input('Digite a nova palavra: ')
        for i in range(len(palavras_sep)):
            if palavras_sep[i] == palavra_substituir:
                palavras_sep[i] = nova_palavra
