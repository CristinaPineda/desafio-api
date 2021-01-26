from flask import Flask, request
from flask_restful import Resource, Api
from gabarito import Gabaritos, EditaGabaritos
from aluno import Alunos, EditaMatriculas
from resposta import RespostasAlunos, EditaRespostas
import json


app = Flask(__name__)
api = Api(app)


"""
dados = json.loads(request.data)
		
		posicao = dados['nome_aluno'] 
		
		return posicao
"""

api.add_resource(CalculoMedia, '/media/<aluno>/<materia>/')

api.add_resource(Gabaritos, '/gabarito/')
api.add_resource(EditaGabaritos, '/gabarito/<int:id>')
api.add_resource(Alunos, '/aluno/')
api.add_resource(EditaMatriculas, '/aluno/<int:id>')
api.add_resource(RespostasAlunos, '/alunoResposta/')
api.add_resource(EditaRespostas, '/alunoResposta/<int:id>')

if __name__ == '__main__':
	app.run(debug=True)

