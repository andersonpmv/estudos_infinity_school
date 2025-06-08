salario_mesal = float(input('Digite o valor do salário: '))
horario_semanal = float(input('Digite as horas trabalhadas na semana: '))

horas_total_mes = horario_semanal*4
salario_hora = salario_mesal/horas_total_mes

print(f'O seu salário por hora é de R$ {salario_hora:.2f}')