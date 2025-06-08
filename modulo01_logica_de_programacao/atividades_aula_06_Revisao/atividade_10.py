# Classificação de Notas:
# Crie um programa que solicite uma nota de 0 a 100
# e informe o conceito (A, B, C, D, F) com base na nota.

nota = int(input('Digite a nota de 0 a 100: '))
if nota > 89:
    print('A')
elif nota > 79:
    print('B')
elif nota > 69:
    print('C')
elif nota > 59:
    print('D')
else:
    print ('F')