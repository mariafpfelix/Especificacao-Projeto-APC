
tarefas = []

tarefas_sugestao = [
    "Começar a compostar",
    "Usar sacolas reutilizáveis no mercado",
    "Evitar uso de canudos",
    "Apagar luzes ao sair de um cômodo",
    "Separar lixo reciclável",
    "Utilizar transporte público ou bicicleta",
    "Reduzir o tempo no banho",
    "Plantar uma árvore",
    "Levar seu próprio copo para o trabalho",
    "Limpar jarros de plantas"
]

def exibir_menu():
    print("\nxxxxxxX Tarefas Ecológicas Xxxxxxx")
    print("1. Adicionar nova tarefa")
    print("2. Remover tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Listar tarefas")
    print("5. Sair")

def adicionar_tarefa():
    print("\nEscolha uma tarefa sustentável do menu ou digite a sua:")
    for i, t in enumerate(tarefas_sugestao):
        print(f"{i + 1}. {t}")
    print("0. Digitar outra tarefa")

    escolha = input("Sua escolha: ")

    if escolha.isdigit() and 1 <= int(escolha) <= len(tarefas_sugestao):
        descricao = tarefas_sugestao[int(escolha) - 1]
    elif escolha == "0":
        descricao = input("Digite a descrição da nova tarefa: ")
    else:
        print("Opção inválida.")
        return

    tarefas.append({"descricao": descricao, "concluida": False})
    print("Tarefa adicionada com sucesso!")

    if "limpar" in descricao.lower():
        print("Parabéns pela boa ação de limpeza!")

def remover_tarefa():
    if not tarefas:
        print("Nenhuma tarefa para remover.")
        return

    listar_tarefas()
    print("Digite o número da tarefa para remover ou '0' para remover todas.")
    try:
        idx = int(input("Sua escolha: ")) - 1
        if idx == -1:
            confirm = input("Tem certeza que deseja remover TODAS as tarefas? (s/n): ")
            if confirm.lower() == 's':
                tarefas.clear()
                print("Todas as tarefas foram removidas.")
        elif 0 <= idx < len(tarefas):
            removida = tarefas.pop(idx)
            print(f"Tarefa '{removida['descricao']}' removida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def marcar_concluida():
    if not tarefas:
        print("Nenhuma tarefa para marcar como concluída.")
        return

    listar_tarefas()
    print("Digite o número da tarefa para concluir ou '0' para marcar todas.")
    try:
        idx = int(input("Sua escolha: ")) - 1
        if idx == -1:
            for tarefa in tarefas:
                tarefa["concluida"] = True
            print("Parabéns, você está tornando o mundo um lugar melhor!")
            print("Todas as tarefas foram marcadas como concluídas.")
        elif 0 <= idx < len(tarefas):
            tarefas[idx]["concluida"] = True
            print("Parabéns, você está tornando o mundo um lugar melhor!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nSuas tarefas sustentáveis:")
        for i, tarefa in enumerate(tarefas):
            status = "✔️" if tarefa["concluida"] else "❌"
            print(f"{i + 1}. {tarefa['descricao']} [{status}]")

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        remover_tarefa()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        listar_tarefas()
    elif opcao == "5":
        print("Encerrando programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
