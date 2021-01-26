from flask import Flask, request
from flask_restful import Resource, Api
import json

#cadastro de alunos 

#variável para armazenar os alunos
listaAlunos = [
	{
		"id": "1",
		'nome_aluno': 'Cristina Pineda',		
	}
]
			
class Alunos(Resource):
	# cadastra novos alunos
	def post(self):
		numeroAlunos = 0
		while (numeroAlunos <= 99):
			dados = json.loads(request.data)
			aluno = len(listaAlunos)
			dados['nome_aluno'] = aluno
			listaAlunos.append(dados)
			numeroAlunos = numeroAlunos+1
			return listaAlunos[aluno]
		else:
			return 'Esse aluno não pode ser cadastrado, o número máximo de alunos é 100!'

		

	# lista de todos os gabaritos já inclusos
	def get(self):
		return listaAlunos



class EditaMatriculas(Resource):
	#consulta modifica e deleta dados dos alunos
	def get(self, id):
		try:
			resposta = listaAlunos[id]
		except IndexError:
			mensagem = 'Aluno {} não existe!'.format(id)
			resposta = {'status': 'erro', 'mensagem': mensagem}
		except Exception:
			mensagem = 'Erro desconhecido'
			resposta = {'status': 'erro', 'mensagem':mensagem}
		return resposta

	def put(self, id):
		dados = json.loads(request.data)
		listaAlunos[id] = dados
		return dados

	def delete(self, id):
		listaAlunos.pop(id)
		return {'status':'sucesso','mensagem':'aluno excluido'}


#URN
#api.add_resource(Alunos, '/aluno/')
#api.add_resource(EditaMatricula, '/aluno/<int:id>')