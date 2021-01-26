### API HTTP

#Api Flask Restful em Python 

*O Desafio*

*A escola Alf aplica provas de múltipla escolha para os alunos. A nota do aluno na prova é determinada pela média ponderada das questões com os pesos de cada questão. Cada questão correta soma 1 ponto multiplicada pelo peso e cada questão errada 0. A nota final é a média aritmética das notas de todas as provas.*



##Exemplo de requisição para cadastrar e modificar gabarito

	{	
		"id": 0
        "materia": "matematica",
        "respostas": [
            {
                "1": "A",
                "2": "B",
                "3": "C"
            }
        ]
    }


##Exemplo de requisição para cadastrar alunos 

	{
        "id": "1",
        "nome_aluno": "Cristina Pineda"
    }


##Exemplo de requisção para cadastrar respostas de alunos 

	{
        "id": "2",
        "nome_aluno": "Isabel pineda",
        "materia": "Matemática",
        "respostasProva": [
            {
                "1": "A",
                "2": "B",
                "3": "C"
            }
        ]
    }