lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Lados inválidos")
elif lado1 == lado2 == lado3:
    print("Triângulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isosceles")
else:
    print("Triângulo escaleno")
