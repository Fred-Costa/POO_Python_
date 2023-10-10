class CarrinhoCompras:
    def __init__(self):
        self.itens = []

    def addProdutos(self, item):
        self.itens.append(item)

    def total(self):
        total = 0
        for item in self.itens:
            total += item.preco * item.qtd
        return print(f"O total no carrinho é de: {total} \n")

    def listar(self):
        for item in self.itens:
            print(f"Item: {item.nome}, Preço: {item.preco}, Quantidade: {item.qtd} \n")