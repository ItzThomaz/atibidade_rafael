logindata = {}
carrinho = {}
historico = {}
entrada = 0
catalogo = {
    'camiseta': {'quantidade': 50, 'descricao': 'Camiseta básica em algodão', 'preco': 20.0},
    'calça jeans': {'quantidade': 30, 'descricao': 'Calça jeans slim fit', 'preco': 100.0},
    'sapato': {'quantidade': 20, 'descricao': 'Sapato social de couro', 'preco': 150.0},
    'meia': {'quantidade': 100, 'descricao': 'Meia confortável para o dia a dia', 'preco': 10.0},
    'boné': {'quantidade': 40, 'descricao': 'Boné ajustável com logo bordado', 'preco': 25.0},
    'jaqueta': {'quantidade': 15, 'descricao': 'Jaqueta corta-vento impermeável', 'preco': 200.0},
    'shorts': {'quantidade': 25, 'descricao': 'Shorts esportivo para atividades físicas', 'preco': 30.0},
    'mochila': {'quantidade': 10, 'descricao': 'Mochila resistente com compartimentos', 'preco': 120.0},
    'luvas': {'quantidade': 35, 'descricao': 'Luvas de couro para o inverno', 'preco': 80.0},
    'óculos de sol': {'quantidade': 50, 'descricao': 'Óculos de sol com proteção UV', 'preco': 150.0}
}

def comprar_produto(prod, quantidade):
    if prod in catalogo:
        produto = catalogo[prod]
        estoque_new = produto['quantidade']
        if quantidade <= estoque_new:
            produto['quantidade'] -= quantidade
            if prod in carrinho:
                carrinho[prod]['quantidade'] += quantidade
            else:
                carrinho[prod] = {'quantidade': quantidade, 'preco': produto['preco']}
            print(f"Você comprou {quantidade} unidade(s) de {prod}.")
        else:
            print(f"Desculpe, não temos estoque suficiente de {prod}. Temos apenas {estoque_new} unidade(s).")
    else:
        print(f"Desculpe, o produto {prod} não está disponível no catálogo.")

def remover_produto(prod, quantidade):
    if prod in carrinho:
        if quantidade <= carrinho[prod]['quantidade']:
            carrinho[prod]['quantidade'] -= quantidade
            if carrinho[prod]['quantidade'] == 0:
                del carrinho[prod]
            catalogo[prod]['quantidade'] += quantidade
            print(f"Você removeu {quantidade} unidade(s) de {prod} do carrinho.")
        else:
            print(f"Você não tem {quantidade} unidade(s) de {prod} no carrinho. Você tem apenas {carrinho[prod]['quantidade']} unidade(s).")
    else:
        print(f"O produto {prod} não está no seu carrinho.")

def finalizar_compra():
    global carrinho, historico
    subtotal = sum(item['quantidade'] * item['preco'] for item in carrinho.values())
    print(f"Subtotal: R${subtotal:.2f}")
    print("Selecione a forma de pagamento:")
    print("1-Cartão de crédito")
    print("2-Cartão de débito")
    print("3-Pagamento via PIX")
    input(": ")
    if carrinho:
        for produto, detalhes in carrinho.items():
            if produto in historico:
                historico[produto]['quantidade'] += detalhes['quantidade']
            else:
                historico[produto] = {'quantidade': detalhes['quantidade'], 'preco': detalhes['preco']}
        carrinho = {}
        print("Compra finalizada com sucesso. Seu carrinho foi esvaziado.")
    else:
        print("Seu carrinho está vazio. Não há nada para finalizar.")

def imprimir_catalogo(a):
    print("Catálogo de Produtos:")
    for produto, detalhes in a.items():
        print(f"Produto: {produto}")
        print(f"  Quantidade disponível: {detalhes['quantidade']}")
        print(f"  Descrição: {detalhes['descricao']}")
        print(f"  Preço: R${detalhes['preco']:.2f}")
        print()

def cadastro(a, b, c):
    logindata[a] = c
    logindata[b] = c

def login(a, b, c):
    if c == logindata.get(a) or c == logindata.get(b):
        print("Login realizado com sucesso!")
        entrada = 1
        return entrada
    else:
        print("Senha ou usuário errado.")
        entrada = 0
        return entrada

while True:
    print("1-realizar cadastro")
    print("2-realizar login")
    dcs = int(input(": "))
    if dcs == 1:
        email = input("Digite o seu Email:")
        user = input("Digite o seu nome: ")
        password = input("Digite a sua senha: ")
        cadastro(email, user, password)
    elif dcs == 2:
        x = 0
        user = input("Digite o nome ou email: ")
        password = input("Digite a senha: ")
        entrada = login(user, x, password)
    if entrada == 1:
        while True:
            print("1-Exibir catálogo")
            print("2-Adicionar produto ao carrinho")
            print("3-Remover produto do carrinho")
            print("4-Exibir carrinho")
            print("5-Finalizar compra")
            print("6-Exibir histórico de compra")
            dcz = int(input(": "))
            if dcz == 1:
                imprimir_catalogo(catalogo)
            elif dcz == 2:
                produto = input("Digite o nome do produto a ser comprado: ")
                qntd = int(input("Digite a quantidade a ser comprada: "))
                comprar_produto(produto, qntd)
            elif dcz == 3:
                produto = input("Digite o nome do produto a ser removido: ")
                qntd = int(input("Digite a quantidade a ser removida: "))
                remover_produto(produto, qntd)
            elif dcz == 4:
                print("Carrinho de Compras:", carrinho)
            elif dcz == 5:
                finalizar_compra()
            elif dcz == 6:
                print("Histórico de Compras:", historico)
