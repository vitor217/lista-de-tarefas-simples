import time
import os
def retornar_ao_menu():
    input("Digite uma tecla para retornar ao menu principal: ")
    main()
def exibir_nome():
    print("""
██╗░░░░░██╗░██████╗████████╗░█████╗░  ██████╗░███████╗
██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
██║░░░░░██║╚█████╗░░░░██║░░░███████║  ██║░░██║█████╗░░
██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║  ██║░░██║██╔══╝░░
███████╗██║██████╔╝░░░██║░░░██║░░██║  ██████╔╝███████╗
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░╚══════╝

████████╗░█████╗░██████╗░███████╗███████╗░█████╗░░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
░░░██║░░░███████║██████╔╝█████╗░░█████╗░░███████║╚█████╗░
░░░██║░░░██╔══██║██╔══██╗██╔══╝░░██╔══╝░░██╔══██║░╚═══██╗
░░░██║░░░██║░░██║██║░░██║███████╗██║░░░░░██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░""")
def exibir_opcoes():
    print("""      1. Adicionar tarefa
      2. Listar tarefas
      3. Mudar estado da tarefa
      4. Remover tarefa
      5. Sair""")
def main():
    os.system("cls")
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()
def opcao_invalida():
    print("Opção invalida.")
    main()
tarefas = [{"nome":"Praça", "estado":False}]
def escolher_opcoes(): 
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        nova_tarefa = input("Digite uma tarefa: ")
        estado = input("Digite o estado da sua tarefa[True para ativado/False para desativado]: ")
        dados = {"nome":nova_tarefa, "estado":estado}
        tarefas.append(dados)
        print("Adicionando tarefa...")
        time.sleep(2)
        print("Tarefa adicionada com sucesso.")
        retornar_ao_menu()
    elif opcao == 2:
        print("Exibindo tarefas...")
        time.sleep(2)
        for tarefa in tarefas:
            nome_tarefa = tarefa["nome"]
            estado = tarefa["estado"]
            print(nome_tarefa, estado)
        retornar_ao_menu()
    elif opcao == 3:
        tarefa_para_mudar_estado = input("Digite o nome da tarefa que deseja marcar como conluída: ")
        for  tarefa in tarefas:
            if tarefa_para_mudar_estado == tarefa["nome"]:
                tarefa_para_mudar_estado = True
                tarefa["estado"] = not tarefa["estado"]
                msg = "A tarefa foi ativada com sucesso" if tarefa["estado"] else "A tarefa foi desativada."
                print(msg)
        retornar_ao_menu()
    elif opcao == 4:
        tarefa_a_ser_removida = str(input("Digite qual tarefa deseja remover: "))
        for tarefa in tarefas:
            if tarefa_a_ser_removida == tarefa["nome"]:
                tarefas.remove(tarefa)
                print("Removendo tarefa...")
                time.sleep(2)
                print("tarefa {} removida com sucesso.".format(tarefa_a_ser_removida))
            else:
                print("Tarefa não encontrada.")
        retornar_ao_menu()
    elif opcao == 5:
        print("Programa encerrado.")
        os.system("cls")
    else:
        opcao_invalida()
if __name__ == "__main__":
    main()