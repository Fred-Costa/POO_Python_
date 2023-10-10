from carrinhoCompras import CarrinhoCompras
from itemCompra import ItemCompra

# Cria produtos pra comprar
item1 = ItemCompra("Lápis", 1.00, 10)
item2 = ItemCompra("Borracha", 0.50, 2)
item3 = ItemCompra("Caderno", 2.50, 5)
item4 = ItemCompra("Portátil", 500.00, 1)
item5 = ItemCompra("Teclado", 100.00, 1)


# cria objeto para fazer os varios metodos na classe Carrinho
carro_compras = CarrinhoCompras()


# Adiciona os produtos ao carro
carro_compras.addProdutos(item1)
carro_compras.addProdutos(item2)
carro_compras.addProdutos(item3)
carro_compras.addProdutos(item4)
carro_compras.addProdutos(item5)


# Faz o total da compra de todos os itens
total_compra = carro_compras.total()


# Lista os produtos do carrinho
carro_compras.listar()