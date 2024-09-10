idade = int(input("Digite a sua idade: "))

if idade < 12:
    print("Você é criança")
elif 12 <= idade < 18:
    print("Você é adolescente")
elif 18 <= idade <= 60:
    print("Você é adulto")
else:
    print("Você é idoso")