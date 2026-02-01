import time
import os

saldo = float(input("Digite seu saldo: R$"))

def exibir_opcoes():
    print("""1. Ver saldo
2. Sacar
3. Depositar
4. Sair
""")

def ver_saldo():
    print(f"Saldo disponível: R${saldo}")
    input("Digite qualquer tecla para voltar ao menu inicial: ")
    print("Voltando à tela inicial...")
    time.sleep(2)
    os.system("cls")
    main()

def sacar():
    global saldo
    valor_saque = float(input("Quanto deseja sacar: "))
    if valor_saque < 0:
        print("Valor inválido.")
        print("Voltando à tela inicial...")
        time.sleep(2)
        os.system("cls")
        main()
    elif valor_saque > saldo:
        print("Saldo indisponível.")
        print("Voltando à tela inicial...")
        time.sleep(2)
        os.system("cls")
        main()
    elif valor_saque <= saldo:
        saldo -= valor_saque
        print("Saque realizado com sucesso.")
        print(f"Valor sacado: R${valor_saque}")
        print(f"Valor disponível na conta: R${saldo}")
        print("Voltando à tela inicial...")
        time.sleep(2)
        os.system("cls")
        main()
    if valor_saque < 0:
        print("Valor inválido.")
        print("Voltando à tela inicial...")
        time.sleep(2)
        os.system("cls")
        main()

def depositar():
    global saldo
    valor_deposito = float(input("Quanto deseja depositar: "))
    saldo += valor_deposito
    print("Valor depositado com sucesso.")
    print(f"Valor depositado: R${valor_deposito}")
    print(f"Valor disponível na conta: R${saldo}")
    print("Voltando à tela inicial...")
    time.sleep(2)
    os.system("cls")
    main()
    if valor_deposito <= 0:
        print("Valor inválido.")
        print("Voltando à tela inicial...")
        time.sleep(2)
        os.system("cls")
        main()

def escolher_opcao():
    opcao = int(input("Digite qual opção deseja: "))
    if opcao == 1:
        ver_saldo()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        depositar()
    elif opcao == 4:
        print("Saindo...")
        time.sleep(2)
        os.system("cls")
    else:
        print("Opção inválida.")
        print("Voltando à tela inicial...")
        time.sleep(2)
        os.system("cls")
        main()       

def main():
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
