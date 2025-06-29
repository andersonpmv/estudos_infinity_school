# ✅ 4. Verificador de vogais
# Enunciado:
# Crie uma função eh_vogal(letra) que receba uma letra e retorne True se for uma vogal, e False caso contrário.

def eh_vogal (letra):
    vogais = 'aeiou'
    return letra in vogais
letra = input('Digite uma letra: ').lower()

print(eh_vogal(letra))