ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

if idade < 0 or idade > 120:
    print("Idade Inválida")
elif idade < 12:
    print("Criança")
elif 12 <= idade < 18:
    print("Adolescente")
elif 18 <= idade < 65:
    print("Adulto")
else:
    print("Idoso")
