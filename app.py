from flask import Flask, request
from flask_restful import Resource, Api
from gabarito import Gabaritos, EditaGabaritos, disciplina
from aluno import Alunos, EditaMatriculas
from resposta import RespostasAlunos, EditaRespostas, respostaAlunos
import json


app = Flask(__name__)
api = Api(app)

#Recebe a lista dos aprovados 
aprovados = []

#Recebe todas notas dos alunos 
notas = []

respostas = respostaAlunos
gabarito = disciplina

class Test(Resource):
	def get(self):
		return gabarito

class CalculoNotaProva(Resource):
	#calcula nota da prova
	def get(self, aluno, materiaProva, ano):
		aluno = next((a for a in respostas if a['nome_aluno'] == aluno), None)
		materiaProva = next((m for m in respostas if m['materia'] == materiaProva), None)
		respostaDoAluno = aluno['respostasProva']
		ano = next((r for r in gabarito if r['ano'] == ano), None)
		respostaGabarito = ano['respostas']

		acertos = []
		for escolha, gabarita in zip(respostaDoAluno, respostaGabarito):
		  if escolha == gabarita:
		    acertos.append(1)
		  else:
		    acertos.append(0)

		nnota = 0
		if acertos[0] == 1:
			nnota = nnotas + 1
		if acertos[1] == 1:
			nnota = nnota + 1
		if acertos[2] == 1:
			nnota = nnota + 2
		if acertos[3] == 1:
			nnota = nnota + 3
		if acertos[4] == 1:
			nnota = nnota + 3	

		notas = nnota/5
		
		notas.append({"aluno": aluno['nome_aluno'], "nota": notas})

		return notas

class Media(Resource):
	#calculo da média
	def get(self, aluno):
		aluno = next((a for a in notas if a['aluno'] == aluno), None)
		lista_notas = aluno['nota']
		media = sum(lista_notas)/len(lista_notas)

		if media <= 7:
			aprovados.append({"aluno": aluno['nome_aluno'], "media": media})
		return media


class Aprovados(Resource):
	#lista dos aprovados
	def get(self):
		return aprovados


api.add_resource(Aprovados, '/aprovados/')
api.add_resource(Media, '/media/<aluno>')
api.add_resource(CalculoNotaProva, '/media/<aluno>/<materiaProva>/<ano>/')

api.add_resource(Gabaritos, '/gabarito/')
api.add_resource(EditaGabaritos, '/gabarito/<int:id>')
api.add_resource(Alunos, '/aluno/')
api.add_resource(EditaMatriculas, '/aluno/<int:id>')
api.add_resource(RespostasAlunos, '/alunoResposta/')
api.add_resource(EditaRespostas, '/alunoResposta/<int:id>')

if __name__ == '__main__':
	app.run(debug=True)

