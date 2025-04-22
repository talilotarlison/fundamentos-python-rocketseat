# lista de tarefas
tarefas = []

# funcao para excluir tarefas concluídas
def excluir_concluidas():
    global tarefas
    # metodo de exclusão de tarefas 1
    # tarefas = [tarefa for tarefa in tarefas if not tarefa["concluida"]]

    # metodo de exclusão de tarefas 2
    for tarefa in tarefas[:]:
        if tarefa["concluida"]:
            tarefas.remove(tarefa)
    line()
    print("Tarefas concluídas excluídas com sucesso!")

# funcao para marcar tarefa como concluída
def marcar_concluida():
    listar_tarefas()
    line()
    print("Marcar tarefa como concluída")
    indice = pegar_index_tarefa("Digite o número da tarefa que deseja marcar como concluída: ")
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Tarefa inválida.")


# funcao para atulizar as tarefas
def atualizar_tarefa():
    listar_tarefas()
    line()
    print("Atualizar Tarefa")
    indice = pegar_index_tarefa("Digite o número da tarefa que deseja atualizar: ")
    if indice >= 0 and indice <= len(tarefas):
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        tarefas[indice]["descricao"] = nova_descricao
        print("Tarefa atualizada com sucesso!")
    else:
        print("Tarefa inválida.")

# funcao que pega index da tarefa
def pegar_index_tarefa(placeholder):
    num_tarefa = int(input(placeholder))
    return num_tarefa - 1

# funcao de lista todas as tarefas
def listar_tarefas():
    if not tarefas:
        line()
        print("Nenhuma tarefa cadastrada.")
        line()
    else:
        line()
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            status = "[x]" if tarefa["concluida"] else "[ ]"
            print(f"{i}.{status} - {tarefa['descricao']}")
        line()


# funcao para criar uma nova tarefa
def criar_tarefa():
    tarefa = input("Digite a descrição da tarefa: ")
    nova_tarefa = {
        "descricao": tarefa,
        "concluida": False
        }

    tarefas.append(nova_tarefa)
    line()
    print('Tarefa criada com sucesso!')
    print(f"Tarefa: {tarefa} - Status: Pendente")
    line()


# funcao de menu da aplicação
def menu():
    print("\nMenu de Tarefas:")
    print("1. Criar Tarefa")
    print("2. Atualizar Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Excluir Tarefas Concluídas")
    print("5. Listar todas Tarefas ")
    print("6. Sair")
    opt = input("Escolha uma opção: ")
    try:
        return int(opt)
    except ValueError:
        print("Por favor, insira um número válido.")
        return menu()

## criar uma linha para separar as opções
def line():
    print("-" * 30)

# funcao main do programa
def main():
    while True:
        opcao = menu()
        if opcao == 1:
            criar_tarefa() #criar tarefa
        elif opcao == 2:
            atualizar_tarefa() # atualizar tarefa
        elif opcao == 3:
            marcar_concluida()
        elif opcao == 4:
            excluir_concluidas()
        elif opcao == 5:
            listar_tarefas() # listar tarefas
        elif opcao == 6:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# chamada da funcão principal
if __name__ == '__main__':
    main()
