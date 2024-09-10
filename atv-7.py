nota_final = float(input(f"\nDigite a sua nota final: "))
frequencia = float(input(f"\nDigite a sua frequência(%): "))

if nota_final >= 7 and frequencia >= 75:
    print(f"\nVocê foi aprovado!\n")
else:
    print(f"\nVocê foi reprovado!\n")