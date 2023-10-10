class ContaBancaria:
    def __init__(self, balance, owner):
        self.__balance = balance
        self.__owner = owner

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
        total = self.__balance
        total += qtd_deposito
        return print(f"Depositou {qtd_deposito}€.")

    def levantar(self, qtd_levantamento):
        total = self.__balance
        if total < qtd_levantamento:
            print("Não tem saldo suficiente...")
        else:
            total -= qtd_levantamento
        return print(f"Levantou {qtd_levantamento}€.")

    def check_balance(self):
        return self.__balance
