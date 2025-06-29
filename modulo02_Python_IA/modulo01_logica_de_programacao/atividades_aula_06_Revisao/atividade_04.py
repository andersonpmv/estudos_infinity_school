# Cálculo de Juros Simples:
# Crie um programa que calcule o valor futuro de um investimento
# usando a fórmula de juros simples. Peça ao usuário para digitar o
# capital inicial, a taxa de juros e o tempo de aplicação.


capital_inicial = float(input('Digite o capital inicial: '))
taxa = float(input('Digite a taxa do juros: '))
tempo = float(input('Digite o tempo do juros em da aplicação (considerar meses):'))

taxa = taxa/100
print(taxa)
calculo_juros = capital_inicial * taxa * tempo

valor_futuro = capital_inicial + calculo_juros

print(f'O valor futuro será de {valor_futuro:.2f}')