import csv  # Biblioteca para trabalhar com arquivos CSV
import os   # Biblioteca para limpar a tela do terminal

# Dicionário para armazenar o usuário logado
usuario_logado = None

# Função para carregar usuários do arquivo CSV
def carregar_usuarios():
    usuarios = []
    try:
        with open("usuarios.csv", mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha:  # Evita linhas vazias
                    usuario = {
                        "login": linha[0],
                        "nome": linha[1],
                        "senha": linha[2],
                        "nivel": linha[3]
                    }
                    usuarios.append(usuario)
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado. Criando um novo...")
    return usuarios

# Função para salvar usuários no arquivo CSV
def salvar_usuarios(usuarios):
    with open("usuarios.csv", mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        for usuario in usuarios:
            escritor.writerow([usuario["login"], usuario["nome"], usuario["senha"], usuario["nivel"]])

# Função para login do usuário
def login(usuarios):
    global usuario_logado
    login_input = input("Digite seu login: ")
    senha_input = input("Digite sua senha: ")

    for usuario in usuarios:  # Aqui, usuários é uma lista de dicionários
        if usuario["login"] == login_input and usuario["senha"] == senha_input:
            usuario_logado = usuario
            print(f"Bem-vindo, {usuario['nome']}! Nível: {usuario['nivel']}")
            return True

    print("Login ou senha incorretos.")
    return False

# Função para criar um novo usuário
def criar_usuario(usuarios):
    login = input("Digite o login do usuário: ")
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    nivel = input("Digite o nível de acesso (gerente, funcionário): ")

    # Criar um dicionário para armazenar os dados do usuário
    novo_usuario = {
        "login": login,
        "nome": nome,
        "senha": senha,
        "nivel": nivel
    }

    # Adiciona o novo usuário à lista de usuários
    usuarios.append(novo_usuario)
    
    print(f"Usuário {nome} criado com sucesso!")

    # Salva a lista de usuários no arquivo
    salvar_usuarios(usuarios)

# Função para listar usuários
def listar_usuarios(usuarios):
    print("\nLista de Usuários:")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:  # Percorre a lista diretamente
            print(f"Login: {usuario['login']}, Nome: {usuario['nome']}, Nível: {usuario['nivel']}")

# Função para atualizar um usuário
def atualizar_usuario(usuarios):
    login = input("Digite o login do usuário que deseja atualizar: ").strip()

    for usuario in usuarios:
        if usuario["login"].lower() == login.lower():
            print(f"Usuário encontrado: {usuario['nome']} ({usuario['nivel']})")
            usuario["nome"] = input("Novo nome: ").strip()
            usuario["senha"] = input("Nova senha: ").strip()
            usuario["nivel"] = input("Novo nível de acesso (gerente, funcionário): ").strip()
            
            print(f"Usuário '{login}' atualizado com sucesso!")
            salvar_usuarios(usuarios)  # Atualiza o arquivo CSV
            return

    print("Usuário não encontrado.")

# Função para remover um usuário
def remover_usuario(usuarios):
    login = input("Digite o login do usuário que deseja remover: ").strip()  # Remove espaços extras

    # Percorre a lista procurando o usuário
    for usuario in usuarios:
        if usuario["login"].lower() == login.lower():  # Comparação sem diferenciar maiúsculas e minúsculas
            usuarios.remove(usuario)  # Remove o usuário da lista
            print(f"Usuário '{login}' removido com sucesso!")
            salvar_usuarios(usuarios)  # Atualiza o arquivo CSV
            return

    print("Usuário não encontrado.")

# Função para carregar produtos do arquivo CSV
def carregar_produtos():
    produtos = {}  # Dicionário para armazenar produtos
    try:
        with open("produtos.csv", "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha:
                    codigo, nome, preco, quantidade = linha
                    produtos[codigo] = {
                        "nome": nome,
                        "preco": float(preco),
                        "quantidade": int(quantidade)
                    }
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado. Criando um novo...")
        with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
            pass  # Apenas cria o arquivo se não existir
    return produtos

# Função para salvar produtos no arquivo CSV
def salvar_produtos(produtos):
    with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        for codigo, dados in produtos.items():
            escritor.writerow([codigo, dados["nome"], dados["preco"], dados["quantidade"]])

# Função para adicionar um novo produto
def adicionar_produto(produtos):
    if usuario_logado["nivel"] != "gerente":
        print("Apenas gerentes podem adicionar produtos.")
        return

    codigo = input("Digite o código do produto: ")
    if codigo in produtos:
        print("Este código já está em uso.")
        return

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    produtos[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
    salvar_produtos(produtos)
    print(f"Produto {nome} adicionado com sucesso!")

# Função para listar todos os produtos
def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\nLista de Produtos:")
    for codigo, dados in produtos.items():
        print(f"Código: {codigo}, Nome: {dados['nome']}, Preço: R${dados['preco']:.2f}, Quantidade: {dados['quantidade']}")
    print()

# Função para buscar um produto por nome ou código
def buscar_produto(produtos):
    termo = input("Digite o nome ou código do produto: ").lower()
    encontrados = [p for c, p in produtos.items() if termo in c.lower() or termo in p["nome"].lower()]

    if encontrados:
        for p in encontrados:
            print(f"Nome: {p['nome']}, Preço: R${p['preco']:.2f}, Quantidade: {p['quantidade']}")
    else:
        print("Produto não encontrado.")

# Função para atualizar um produto
def atualizar_produto(produtos):
    if usuario_logado["nivel"] != "gerente":
        print("Apenas gerentes podem atualizar produtos.")
        return

    codigo = input("Digite o código do produto que deseja atualizar: ")
    if codigo not in produtos:
        print("Produto não encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")

    novo_nome = input("Novo nome: ") or produtos[codigo]["nome"]
    novo_preco = input("Novo preço: ")
    novo_quantidade = input("Nova quantidade: ")

    produtos[codigo] = {
        "nome": novo_nome,
        "preco": float(novo_preco) if novo_preco else produtos[codigo]["preco"],
        "quantidade": int(novo_quantidade) if novo_quantidade else produtos[codigo]["quantidade"]
    }

    salvar_produtos(produtos)
    print(f"Produto {novo_nome} atualizado com sucesso!")

# Função para remover um produto
def remover_produto(produtos):
    if usuario_logado["nivel"] != "gerente":
        print("Apenas gerentes podem remover produtos.")
        return

    codigo = input("Digite o código do produto que deseja remover: ")
    if codigo not in produtos:
        print("Produto não encontrado.")
        return

    del produtos[codigo]
    salvar_produtos(produtos)
    print(f"Produto removido com sucesso!")

def menu():
    produtos = carregar_produtos()
    usuarios = carregar_usuarios()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Login")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sucesso = login(usuarios)
            if sucesso:
                menu_usuario(produtos, usuarios)  # Agora só chama o menu do usuário se o login for bem-sucedido
        elif opcao == "2":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_usuario(produtos, usuarios):
    while True:
        print("\n=== MENU DO SISTEMA ===")
        print("1 - Gerenciar Usuários")
        print("2 - Gerenciar Produtos")
        print("3 - Logout")

        opcao = input("Escolha uma opção: ")

        if opcao == "1" and usuario_logado["nivel"] == "gerente":
            menu_usuarios(usuarios)
        elif opcao == "2":
            menu_produtos(produtos)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida ou permissão insuficiente.")

def menu_usuarios(usuarios):
    while True:
        print("\n=== GERENCIAR USUÁRIOS ===")
        print("1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Remover usuário")
        print("5 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            atualizar_usuario(usuarios)
        elif opcao == "4":
            remover_usuario(usuarios)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

def menu_produtos(produtos):
    while True:
        print("\n=== GERENCIAR PRODUTOS ===")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar produto")
        print("5 - Remover produto")
        print("6 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            buscar_produto(produtos)
        elif opcao == "4":
            atualizar_produto(produtos)
        elif opcao == "5":
            remover_produto(produtos)
        elif opcao == "6":
            break
        else:
            print("Opção inválida.")

# Iniciar o sistema
menu()

