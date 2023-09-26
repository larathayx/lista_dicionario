cidades_estados = {'São Paulo': 'SP','Rio de Janeiro': 'RJ','Belo Horizonte': 'MG','Salvador': 'BA','Recife': 'PE','Fortaleza': 'CE','Porto Alegre': 'RS','Manaus': 'AM','Brasília': 'DF','Curitiba': 'PR',}
estados_unicos = []

for estado in cidades_estados.values():
    if estado not in estados_unicos:
        estados_unicos.append(estado)

print("Estados sem repetição:")
for estado in estados_unicos:
    print(estado)
