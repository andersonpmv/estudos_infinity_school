# festa_sabado = {"Ana", "Bruno", "Carlos", "Duda", "Eduardo", "Fernanda"}
# festa_domingo = {"Carlos", "Eduardo", "Giovana", "Henrique", "Ana"}

# print (f'{festa_sabado & festa_domingo} foram em ambas as festas')

# print (f'{festa_sabado - festa_domingo} foram apenas na festa de sábado')

# print(f'{festa_sabado | festa_domingo} foram em apenas umas das festas')

# print(f'{festa_domingo - festa_sabado} foram apenas na festa de domingo')


conjunto1 = set(input("Digite os elementos do primeiro conjunto, separados por espaço: ").split(','))
conjunto2 = set(input("Digite os elementos do segundo conjunto, separados por espaço: ").split(','))

print(conjunto1 & conjunto2)