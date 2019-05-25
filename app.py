import Agenda
import os

arquivo = "agenda.p"
agenda = Agenda.Agenda(arquivo)

clear = lambda: os.system('clear || cls')

while True:
	clear()

	print("Não se preocupe, use a agenda e nós salvaremos seus contatos automaticamente\n\n",
		"Escolha uma das opções abaixo\n",
		"1 - Inserir contato.\n",
		"2 - Alterar contato.\n",
		"3 - Deletar contatos.\n",
		"4 - Listar contatos.\n",
		"5 - Pesquisar contatos.\n",
		"6 - Sair")
	
	opcao = input()

	if opcao == "1":
		agenda.addPessoas()
	elif opcao != "1" and opcao != "6" and len(agenda.listaDePessoas) == 0:
		print("\nVocê não tem nenhum contato inserido ainda")
	elif opcao == "2":
		agenda.alteraPessoas()
	elif opcao == "3":
		agenda.delPessoas()
	elif opcao == "4":
		agenda.listarPessoas()
	elif opcao == "5":
		agenda.pesquisarPessoas()
	elif opcao == "6":
		break
	else:
		print("\nOpção inválida!")

	input ("\nPressione enter para continuar...")