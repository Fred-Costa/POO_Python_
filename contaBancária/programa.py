from contaBancaria import ContaBancaria

contaFred = ContaBancaria(5000, "Frederico")

print(f"{contaFred.owner} bem-vindo a sua aplicação de banco \n")
print("ESCOLHA UMA DAS OPÇÕES")

while True:
    resposta = int(input("1. Depositar dinheiro na conta \n"
                         "2. Levantar dinheiro da conta \n"
                         "3. Verificar o saldo da conta \n"
                         "4. Fechar aplicação"))

    if resposta == 1:
        deposito = int(input(f"Quanto deseja depositar: "))
        contaFred.depositar(deposito)

    elif resposta == 2:
        levantamento = int(input("Quanto deseja levantar: "))
        contaFred.levantar(levantamento)

    elif resposta == 3:
        contaFred.check_balance()

    elif resposta == 4:
        print("A encerrar a aplicação...")
        break
