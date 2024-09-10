valor_compra = float(input(f"Digite o valor da compra: R$ "))
print(f"\nAVISO: Se o valor for maior que 12 parcelas vai ser acrescentado um juro de 1.5% no valor total, além de um valor de R$ 6 para cada parcela que passar de 12x\n")
parcelas = int(input("Digite o número de parcelas(1 a 24): "))


if parcelas < 1 or parcelas > 24:
    print(f"\nNúmero de parcelas inválido! Escolha entre 1 e 24.")
elif parcelas <= 12:
    valor_parcela = valor_compra / parcelas
    print(f"\nO valor total a ser pago é R$ {valor_compra:.2f}")
    print(f"Cada parcela será de R$ {valor_parcela:.2f}\n")
else:
    valor_com_juros = valor_compra * 1.015
    acrescimo = (parcelas - 12) * 6
    valor_total = valor_com_juros + acrescimo
    valor_parcela = valor_total / parcelas
    print(f"\nO valor total a ser pago é R$ {valor_total:.2f}")
    print(f"Cada parcela será de R$ {valor_parcela:.2f}\n")