dicionario = {'python': 'Uma linguagem de programação de alto nível conhecida por sua simplicidade e legibilidade.','programação': 'O ato de escrever código de computador para realizar tarefas específicas.','algoritmo': 'Um conjunto de passos bem definidos para resolver um problema ou realizar uma tarefa.','dicionário': 'Uma estrutura de dados que mapeia chaves para valores.','loop': 'Uma estrutura de controle que permite a repetição de um bloco de código.',}

while True:
    palavra_chave = input("Digite uma palavra-chave para obter a definição (ou 'sair' para sair): ")

    if palavra_chave == 'sair':
        break 
    if palavra_chave in dicionario:
        definicao = dicionario[palavra_chave]
        print(f"Definição de '{palavra_chave}': {definicao}")
    else:
        print(f"A palavra-chave '{palavra_chave}' não foi encontrada no dicionário.")
