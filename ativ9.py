notas_alunos = {'João': 8.5,'Maria': 7.0,'Pedro': 9.0,'Ana': 6.5,}

soma_notas = sum(notas_alunos.values())
numero_de_alunos = len(notas_alunos)   

if numero_de_alunos > 0:
    media = soma_notas / numero_de_alunos
    print(f"A média das notas dos alunos é: {media}")
else:
    print("Não há notas de alunos no dicionário.")
