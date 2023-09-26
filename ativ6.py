produtos_precos = {'arroz': 2.5,'feijão': 1.0,'macarrão': 1.2,'carne': 10.0,'leite': 2.0,}
lista_de_compras = ['arroz', 'feijão', 'macarrão', 'carne', 'leite']

valor_total = 0

for item in lista_de_compras:
    if item in produtos_precos:
        valor_total += produtos_precos[item]
    else:
        print(f"{item} não está na lista de produtos disponíveis.")

print(f"O valor total da compra é: R${valor_total}")
