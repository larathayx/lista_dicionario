alimentos_calorias = {'Arroz': 150,'Frango grelhado': 200,'Brócolis': 55,'Salada de alface': 10,'Pão integral': 70,'Salmão assado': 300,'Cenoura cozida': 45,}
alimentos_consumidos = ['Arroz', 'Frango grelhado', 'Brócolis', 'Salada de alface']
total_calorias = 0

for alimento in alimentos_consumidos:
    if alimento in alimentos_calorias:
        total_calorias += alimentos_calorias[alimento]
    else:
        print(f"Calorias para {alimento} não encontradas no dicionário.")

print(f"Total de calorias consumidas na refeição: {total_calorias} calorias.")
