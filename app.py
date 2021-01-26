from flask import Flask, request
from flask_restful import Resource, Api
from gabarito import Gabaritos, EditaGabaritos
from aluno import Alunos, EditaMatriculas
import json


app = Flask(__name__)
api = Api(app)



api.add_resource(Gabaritos, '/gabarito/')
api.add_resource(EditaGabaritos, '/gabarito/<int:id>')
api.add_resource(Alunos, '/aluno/')
api.add_resource(EditaMatriculas, '/aluno/<int:id>')

if __name__ == '__main__':
	app.run(debug=True)

