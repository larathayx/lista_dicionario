pessoas_idades = {'João': 30, 'Maria': 25, 'Pedro': 35, 'Ana': 28}
pessoa = 'João'
if pessoa in pessoas_idades:
    idade = pessoas_idades[pessoa]
    print(f"A idade de {pessoa} é {idade} anos.")
else:
    print(f"{pessoa} não está no dicionário.")
