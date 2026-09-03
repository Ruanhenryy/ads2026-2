catalogo = ["Macarrão alfazorro", "Camarão romano", "Sopa de carne", "Refrigerante"]
comanda = {
    "Macarrão alfazorro" : 75.90,
    "Camarão romano" : 65.30,
    "Sopa de carne" : 20.99,
    "Refrigerante" : 30.99,
    "Maizena hidatrada" : 10.00
}

def itens_validos(comanda):
    itensValidos = []
    for item in comanda.keys():
        if item not in catalogo:
            print(f"Item '{item}' não encontrado no catálogo")
        else:
            itensValidos.append(item)
    return itensValidos     

def subtotal(comanda):
    total = 0
    for item, valor in comanda.items():
        if item not in catalogo:
            print(f"Item '{item}' não encontrado no catálogo")
        else:
            total += valor
    return total


def desconto(comanda, valor, minimo=3):
    if len(itens_validos(comanda)) >= minimo:
        return valor * 0.10
    return 0

def fechar(comanda):
    sub = subtotal(comanda)
    desc = desconto(comanda, sub)
    return {"subtotal": sub, "desconto": desc, "total": sub - desc}


print(itens_validos(comanda))
print(subtotal(comanda))
print(desconto(comanda, subtotal(comanda)))
print(fechar(comanda))