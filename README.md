

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