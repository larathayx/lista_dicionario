contatos = {'João': '123-456-7890','Maria': '987-654-3210','Pedro': '555-555-5555',}
contatos['Ana'] = '777-777-7777'

print("Dicionário de Contatos Atualizado:")
for nome, telefone in contatos.items():
    print(f"{nome}: {telefone}")
