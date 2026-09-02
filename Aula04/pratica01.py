servicos = ["Alugar", "Reservar", "Pagar", "Devolver"]

for i, servico in enumerate(servicos, start=1):
    print(f"{i} {servico}")

"""----------------------------------------------------------------------------"""

comanda = {
    "Macarrão alfazorro" : 75.90,
    "Camarão romano" : 65.30,
    "Sopa de carne" : 20.99,
    "Refrigerante" : 30.99
}
total = 0

for valor in comanda.values():
    total += valor

print(f"Total: {total}")

for item in comanda.keys():
    if item in ("Água" , "Sorvete"):
        print("Item não encontrado!")
        continue

"""----------------------------------------------------------------------------"""

valor_corte = 15.00
saldo = 200
contador = 0

while saldo > 14:
    contador += 1
    saldo -= 15

print(f"Quantidade total de cortes {contador}")