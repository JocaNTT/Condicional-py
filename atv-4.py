salario = float(input("Digite o seu salário: R$ "))

if salario <= 1900:
    print("Seu salário está isento de imposto.")
elif 1901 <= salario <= 2800:
    imposto = salario * 0.075
    print(f"O imposto de seu salário é de 7.5%, valor do imposto: R$ {imposto:.2f}")
elif 2801 <= salario <= 3700:
    imposto = salario * 0.15
    print(f"O imposto de seu salário é de 15%, valor do imposto: R$ {imposto:.2f}")
else:
    imposto = salario * 0.225
    print(f"O imposto de seu salário é de 22.5%, valor do imposto: R$ {imposto:.2f}")