filmes_lancamento = {'Filme A': 2010, 'Filme B': 1995, 'Filme C': 2005}
lista_anos = list(filmes_lancamento.values())
lista_ordenada = []

while lista_anos:
    ano_minimo = min(lista_anos)
    lista_ordenada.append(ano_minimo)
    lista_anos.remove(ano_minimo)

print(lista_ordenada)
filmes_lancamento = {'Filme A': 2010, 'Filme B': 1995, 'Filme C': 2005}
lista_anos = list(filmes_lancamento.values())
lista_ordenada = []

while lista_anos:
    ano_minimo = min(lista_anos)
    lista_ordenada.append(ano_minimo)
    lista_anos.remove(ano_minimo)

print(lista_ordenada)
