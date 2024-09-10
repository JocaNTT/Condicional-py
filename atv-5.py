horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: R$ "))

if horas_trabalhadas > 40:
    horas_extras = horas_trabalhadas - 40
    salario_normal = 40 * valor_hora
    bonus_horas_extras = horas_extras * valor_hora * 1.5
    salario_total = salario_normal + bonus_horas_extras
    print(f"Salário com bônus(50%) pelas horas extras: R$ {salario_total:.2f}")
else:
    salario_total = horas_trabalhadas * valor_hora
    print(f"Salário total: R$ {salario_total:.2f}")