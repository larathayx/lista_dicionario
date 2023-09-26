paises_capitais = {'Brasil': 'Brasília','Estados Unidos': 'Washington, D.C.','França': 'Paris','Alemanha': 'Berlim','Japão': 'Tóquio',}

while True:
    pais = input("Digite o nome de um país para obter a capital (ou 'sair' para sair): ")

    if pais.lower() == 'sair':
        break  
    if pais in paises_capitais:
        capital = paises_capitais[pais]
        print(f"A capital de {pais} é {capital}.")
    else:
        print(f"País não encontrado: {pais}")
