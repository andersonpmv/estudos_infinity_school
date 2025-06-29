# Algoritmo de Conversão de Temperatura:
# Crie um algoritmo que converta uma temperatura de Celsius
# para Fahrenheit. Solicite ao usuário a temperatura em Celsius
# e exiba o resultado em Fahrenheit.

celsius = int(input('Digite a temperatura em graus Celsius: '))
fahrenheit = celsius * 9 / 5 + 32
print(f'{fahrenheit:.0f}° F')