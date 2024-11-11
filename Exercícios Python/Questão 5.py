temperatura = float(input("Digite a temperatura em °C: "))

if temperatura < -50 or temperatura > 50:
    print("Inabitável")
elif temperatura < 15:
    print("Muito Frio")
elif 15 <= temperatura <= 20:
    print("Frio")
elif 20 < temperatura <= 25:
    print("Agradável")
elif 25 < temperatura <= 35:
    print("Quente")
else:
    print("Muito Quente")
