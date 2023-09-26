contatos = {'João': '123-456-7890','Maria': '987-654-3210','Pedro': '555-555-5555',}
nome_contato_a_remover = 'Maria'

if nome_contato_a_remover in contatos:
    telefone_removido = contatos.pop(nome_contato_a_remover)
    print(f"Contato removido: {nome_contato_a_remover}, Telefone: {telefone_removido}")
else:
    print(f"{nome_contato_a_remover} não está na lista de contatos.")

print("Dicionário de Contatos Atualizado:")
for nome, telefone in contatos.items():
    print(f"{nome}: {telefone}")
