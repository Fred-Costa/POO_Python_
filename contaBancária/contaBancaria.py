class ContaBancaria:
    def __init__(self, balance, owner):
        self.__balance = balance
        self.__owner = owner
        self.historico = []

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    @property
    def owner(self):
        return self.__owner

    @owner.deleter
    def owner(self):
        del self.__owner

    def depositar(self, qtd_deposito):
        if qtd_deposito > 0:
            total = self.__balance
            total += qtd_deposito
            mensagem = f"Depositou {qtd_deposito}€ com sucesso. \n"
            self.historico.append(mensagem)
            return mensagem
        else:
            return "Valor inválido!"

    def levantar(self, qtd_levantamento):
        if 0 < qtd_levantamento <= self.balance:
            self.__balance -= qtd_levantamento
            mensagem = f"Levantou {qtd_levantamento}€ com sucesso. \n"
            self.historico.append(mensagem)
            return mensagem
        else:
            return "Saldo insuficiente ou valor inválido!"

    def check_balance(self):
        mensagem = f"Atualmente tem: {self.__balance}€ \n"
        self.historico.append(mensagem)
        return mensagem
