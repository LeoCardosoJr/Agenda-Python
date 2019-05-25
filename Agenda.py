import pickle
import re
from Pessoas import Pessoas
from threading import Thread
import os

class Agenda():
	def __init__(self, arquivo):
		self.listaDePessoas = []
		self.arquivo = arquivo
		self.threadSalvarArquivo = []
		self.carregarAgenda()

	def salvaAgendaThread(self):
		thread = Thread(target = self.salvarAgenda)
		thread.start()
		self.threadSalvarArquivo.append(thread)

	def salvarAgenda(self):
		pickle.dump(self.listaDePessoas, open(self.arquivo, "wb"))

	def carregarAgenda(self):
		if os.path.isfile(self.arquivo):
			self.listaDePessoas = pickle.load(open(self.arquivo, "rb" ))

	def addPessoas(self, qtdValores = None):
		try:
			nome = str(input("Digite o nome do contato: "))
			numero = input("Digite o número de telefone do(a) " + str(nome) + ": ")
			numeroFormatado = re.sub('[^0-9]', '', numero)

			if not nome and not numeroFormatado:
				print("Insira nome e número corretamente")
				return 

			self.listaDePessoas.append(Pessoas(nome, numeroFormatado))
			self.salvaAgendaThread()
		except:
			print("Valor inválido! Tente novamente")

	def delPessoas(self, qtdValores = None):		
		listaDeResultados = self.pesquisarPessoas()

		if not listaDeResultados:
			return

		msg = "Digite 'Sim' para deletar todos o(s) contato(s) mostrados da sua lista\n"
		msg += "Se quiser deletar apenas 1, digite o número ao lado do nome\n"
		msg += "Para voltar para o menu principal digite 'Não': "

		opcao = str(input(msg))
		if opcao != "Não":
			try:
				removido = []
				
				if opcao == "Sim":
					for pessoa in listaDeResultados:
						removido = self.listaDePessoas.remove(pessoa)
					self.salvaAgendaThread()

				if opcao.isdigit():
					removido = self.listaDePessoas.remove(listaDeResultados[int(opcao)])
					self.salvaAgendaThread()

				if len(removido) > 0:
					print("Contato removido com sucesso!")
			except:
				pass

	def alteraPessoas(self, qtdValores = None):		
		listaDeResultados = self.pesquisarPessoas()

		if not listaDeResultados:
			return

		msg = "Digite o número ao lado do nome para editar\n"
		msg += "Para voltar para o menu principal digite 'Não': "

		opcao = str(input(msg))
		
		try:
			if opcao.isdigit():
				indice = self.listaDePessoas.index(listaDeResultados[int(opcao)])
				nome = str(input("Digite o nome do contato: "))
				numero = input("Digite o número de telefone do(a) " + str(nome) + ": ")
				numeroFormatado = re.sub('[^0-9]', '', numero)

				if not nome and not numeroFormatado:
					print("Insira nome e número corretamente")
					return 
					
				self.listaDePessoas[indice].alterarDados(nome, numeroFormatado)
				self.salvaAgendaThread()
			else:
				print("Necessário escolher o número do usuário para editar")
		except:
			pass

	def pesquisarPessoas(self):
		nome = str(input("Digite o nome completo ou incio do nome do contato: "))
		listaDeResultados = list(filter(lambda x: x.nome.startswith(nome), self.listaDePessoas))

		if len(listaDeResultados) == 0:
			print("Sem resultados para a busca")
			return

		for pessoa in listaDeResultados:
			print(str(listaDeResultados.index(pessoa)) + " - " + pessoa.getPessoa())

		return listaDeResultados

	def listarPessoas(self):
		for pessoa in self.listaDePessoas:
			print(pessoa.getPessoa())

	def __del__(self):				
		for x in self.threadSalvarArquivo:
			x.join()
		
		print("Terminando de salvar seus contatos")