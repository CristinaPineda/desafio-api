from flask import Flask, request
from flask_restful import Resource, Api
import json

#cadastro de gabaritos 

#variável para armazenar os gabaritos
disciplina = [
	{
		"id": "1",
		'materia': 'matematica',
		'respostas': [{'1':'A',
				   		'2':'B',
				  	 	'3':'D'}
				 	]		
	}
]
			
class Gabaritos(Resource):
	# cadastra novos gabaritos
	def post(self):
		dados = json.loads(request.data)
		posicao = len(disciplina)
		dados['materia'] = posicao
		disciplina.append(dados)
		return disciplina[posicao]

	# lista de todos os gabaritos já inclusos
	def get(self):
		return disciplina



class EditaGabaritos(Resource):
	#consulta modifica e deleta dados do gabarito
	def get(self, id):
		try:
			response = disciplina[id]
		except IndexError:
			mensagem = 'Gabarito {} não existe!'.format(id)
			response = {'status': 'erro', 'mensagem': mensagem}
		except Exception:
			mensagem = 'Erro desconhecido'
			response = {'status': 'erro', 'mensagem':mensagem}
		return response

	def put(self, id):
		dados = json.loads(request.data)
		disciplina[id] = dados
		return dados

	def delete(self, id):
		disciplina.pop(id)
		return {'status':'sucesso','mensagem':'registro excluido'}


#URN
#api.add_resource(Gabaritos, '/gabarito/')
#api.add_resource(EditaGabaritos, '/gabarito/<int:id>')