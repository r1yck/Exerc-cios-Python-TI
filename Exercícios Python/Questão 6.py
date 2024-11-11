distancia = float(input("Digite a distância percorrida (em km): "))
combustivel = float(input("Digite o total de combustível usado (em litros): "))

if combustivel <= 0 or distancia <= 0:
    print("Dados inválidos")
else:
    consumo = distancia / combustivel
    if consumo < 8:
        print("Consumo alto")
    elif 8 <= consumo <= 12:
        print("Consumo moderado")
    else:
        print("Consumo econômico")
