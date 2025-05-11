codigo, quanti, valor_uni = input().split(" ")
codigo = int(codigo)
quanti = int(quanti)
valor_uni = float(valor_uni)

codigo2, quanti2, valor_uni2 = input().split(" ")
codigo2 = int(codigo2)
quanti2 = int(quanti2)
valor_uni2 = float(valor_uni2)

total = quanti * valor_uni + quanti2 * valor_uni2
print(f"VALOR A PAGAR: R$ {total:.2f}")