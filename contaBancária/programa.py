import os
from contaBancaria import ContaBancaria

dir = r"C:\Users\frede\IdeaProjects\POO-exercises\contaBancária"
arquivos = os.listdir(dir)
nome_arquivo = "histórico.txt"

contaFred = ContaBancaria(5000, "Frederico")

print(f"{contaFred.owner} bem-vindo a sua aplicação de banco \n")
print("ESCOLHA UMA DAS OPÇÕES")

if nome_arquivo not in arquivos:
    with open(nome_arquivo, "a+", encoding="utf-8") as file:
        file.write("Histórico da conta bancária de " + contaFred.owner + "\n")

while True:
    resposta = int(input("1. Depositar dinheiro na conta \n"
                         "2. Levantar dinheiro da conta \n"
                         "3. Verificar o saldo da conta \n"
                         "4. Fechar aplicação \n"))

    with open(nome_arquivo, "a", encoding="utf-8") as file:
        if resposta == 1:
            deposito = int(input(f"Quanto deseja depositar: "))
            file.write(contaFred.depositar(deposito))

        elif resposta == 2:
            levantamento = int(input("Quanto deseja levantar: "))
            file.write(contaFred.levantar(levantamento))

        elif resposta == 3:
            file.write(contaFred.check_balance())

        elif resposta == 4:
            print("A encerrar a aplicação...")
            break
