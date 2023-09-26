jogadores_gols = {'Cristiano Ronaldo': [3, 2, 1, 4, 2],'Lionel Messi': [2, 3, 2, 1, 3],'Neymar Jr.': [1, 0, 2, 2, 1]}
mais_gols = 0
melhor_jogador = ''

for jogador, gols in jogadores_gols.items():
    total_gols = sum(gols)
    if total_gols > mais_gols:
        mais_gols = total_gols
        melhor_jogador = jogador

print(f'O jogador com mais gols é {melhor_jogador} com um total de {mais_gols} gols.')