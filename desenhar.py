import os

def desenhar_arvore(pasta, nivel=0):
    # Lista os arquivos e pastas no caminho atual
    conteudo = os.listdir(pasta)

    # Ignora pastas e arquivos específicos
    ignorar = ['.git', '.venv', '__pycache__', 'venv']
    for item in conteudo:
        # Ignora arquivos e pastas listadas na variável ignorar
        if item in ignorar:
            continue
        # Adiciona espaços para representar a hierarquia
        espacos = "|   " * nivel + "|-- "
        # Imprime o item
        print(espacos + item)
        # Verifica se o item é uma pasta
        proximo_item = os.path.join(pasta, item)
        if os.path.isdir(proximo_item):
            # Chama a função recursivamente para a próxima pasta
            desenhar_arvore(proximo_item, nivel + 1)
    
# Pasta raiz do projeto
pasta_raiz = '.'
# Desenha a árvore a partir da pasta raiz
desenhar_arvore(pasta_raiz)
