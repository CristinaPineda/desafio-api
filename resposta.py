from flask import Flask, request
from flask_restful import Resource, Api
import json

#cadastro de alunos 

#variável para armazenar respostas dos alunos
respostaAlunos = [
	{
		"id": "1",
		"nome_aluno": "Cristina",
		"materia": "matematica",
		"respostasProva": [{"1":"A",
				   		"2":"B",
				  	 	"3":"D"}
				 	]		
	}
]
			
class RespostasAlunos(Resource):
	# respostas dos alunos
	def post(self):
		dados = json.loads(request.data)
		respostas = len(respostaAlunos)
		respostaAlunos.append(dados)	
		return respostaAlunos[respostas]		

	# lista de respostas já inclusas
	def get(self):
		return respostaAlunos



class EditaRespostas(Resource):
	#modifica e deleta respostas dos alunos
	def put(self, id):
		dados = json.loads(request.data)
		respostaAlunos[id] = dados
		return dados

	def delete(self, id):
		respostaAlunos.pop(id)
		return {'status':'sucesso','mensagem':'resposta excluida'}


#URN
#api.add_resource(RespostasAlunos, '/alunoResposta/')
#api.add_resource(EditaRespostas, '/alunoResposta/<int:id>')