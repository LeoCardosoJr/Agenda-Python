class Pessoas:
	def __init__(self, nome, telefone):
		self.nome = nome
		self.telefone = telefone

	def alterarDados(self, nome, telefone):
		self.nome = nome
		self.telefone = telefone

	def getPessoa(self):
		return self.nome + " - " + str(self.telefone)

# import pickle
# lista = [Pessoas("Leo", 123), Pessoas("Gustavo", 456)]
# result = list(filter(lambda x: x.nome.startswith("Gust"), lista))
# pickle.dump( result, open( "save.p", "wb" ) )
# favorite_color = pickle.load( open( "save.p", "rb" ) )
# print(favorite_color[0].getPessoa())
# print(pickle.loads(pickle.dumps(result[0])).default())
# print(json.loads(json.dumps(result[0].__dict__)).getPessoas)