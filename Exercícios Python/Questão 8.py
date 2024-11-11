total = 0
pares = 0
impares = 0

while True:
    numero = int(input("Digite um número inteiro (negativo para parar): "))
    
    if numero < 0:
        break
    
    total += 1
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Calculando as porcentagens
if total > 0:
    porcentagem_pares = (pares / total) * 100
    porcentagem_impares = (impares / total) * 100
    print(f"Total de números: {total}")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")
    print(f"Porcentagem de números pares: {porcentagem_pares:.2f}%")
    print(f"Porcentagem de números ímpares: {porcentagem_impares:.2f}%")
else:
    print("Nenhum número válido foi informado.")
