def calcular_produto1(quantidade):
    preco_unitario = 10
    if 1 <= quantidade <= 5:
        total = preco_unitario * quantidade
    elif 6 <= quantidade <= 10:
        total = preco_unitario * quantidade * 0.95  # 5% de desconto
    elif 11 <= quantidade <= 50:
        total = preco_unitario * quantidade * 0.90  # 10% de desconto
    elif quantidade > 50:
        total = preco_unitario * quantidade * 0.80  # 20% de desconto
    return total

def calcular_produto2(peso):
    preco_kg = 16.50
    if peso <= 10:
        total = preco_kg * peso
    else:
        pacotes = peso // 10
        if pacotes > 10:
            return "Compra de mais de 10 pacotes não é permitida."
        total = pacotes * 10 * preco_kg * 0.95  # 5% de desconto por pacote
    return total

def calcular_pagamento(total, parcelas):
    if parcelas == 1:
        total *= 0.90  # 10% de desconto
    elif parcelas >= 3:
        total *= 1.05  # 5% de juros
    # Se for 2 parcelas, não há alteração no valor.
    return total


def calcular_preco_final(quantidade_produto1, peso_produto2, parcelas):

    preco_produto1 = calcular_produto1(quantidade_produto1)
    
    preco_produto2 = calcular_produto2(peso_produto2)
    
    # Verificar se a compra do produto 2 foi válida
    if isinstance(preco_produto2, str):
        return preco_produto2  # Se for uma mensagem de erro, retornar
    
    preco_total = preco_produto1 + preco_produto2
    
    # Aplicar a forma de pagamento
    preco_final = calcular_pagamento(preco_total, parcelas)
    
    return preco_final

quantidade_produto1 = int(input("Digite a quantidade do produto 1: "))
peso_produto2 = float(input("Digite o peso do produto 2 (em kg): "))
parcelas = int(input("Digite a quantidade de parcelas (1, 2 ou 3+): "))

preco_final = calcular_preco_final(quantidade_produto1, peso_produto2, parcelas)
print(f"O preço final é: R${preco_final:.2f}")
