class ItemCompra:
    def __init__(self, nome, preco, qtd):
        self.__nome = nome
        self.__preco = preco
        self.__qtd = qtd

    # Getters
    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def qtd(self):
        return self.__qtd
