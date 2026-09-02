valor = float(input("Digite o valor do frete: "))
cupom = input("Digite se você tem cupom: S/N")

frete = 0
if cupom.lower == "s" or valor > 300:
    frete = 0
elif valor > 100 and valor < 300:
    frete = 8
elif valor < 100:
    frete = 13

