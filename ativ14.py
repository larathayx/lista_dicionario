frutas_quantidades = {'Maçã': 20,'Banana': 30,'Uva': 15,'Laranja': 25,'Pera': 18,}
fruta_maior_quantidade = None
maior_quantidade = 0

for fruta, quantidade in frutas_quantidades.items():
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        fruta_maior_quantidade = fruta

if fruta_maior_quantidade:
    print(f"A fruta com a maior quantidade é {fruta_maior_quantidade} com {maior_quantidade} unidades.")
else:
    print("Não há frutas no dicionário.")
