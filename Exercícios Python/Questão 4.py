distancia = float(input("Digite a distância em km: "))

if distancia < 1:
    print("Ir a pé")
elif 1 <= distancia <= 5:
    print("Usar bicicleta")
elif 5 < distancia <= 20:
    print("Usar transporte público")
elif distancia > 20:
    print("Usar carro")
else:
    print("Distância inválida")
