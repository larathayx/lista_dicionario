produtos_estoques = {'Arroz': 50,'Feijão': 40,'Macarrão': 30,'Carne': 20,'Leite': 10}
estoque_minimo = 25
produtos_com_estoque_baixo = {}

for produto, estoque in produtos_estoques.items():
    if estoque < estoque_minimo:
        produtos_com_estoque_baixo[produto] = estoque

print("Produtos com estoque abaixo de", estoque_minimo, ":")
for produto, estoque in produtos_com_estoque_baixo.items():
    print(f"{produto}: {estoque} unidades")
