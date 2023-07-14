from pydantic import BaseModel
from typing import List
from model.aluno import Aluno

class AlunoSchema(BaseModel):
    """ Define como um novo aluno a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "Aluno da Silva"
    data_nascimento: str = "05/05/2013"
    sexo: str = "Masculino"
    nome_responsavel: str = "Responsavel da Silva"


class ListagemAlunosSchema(BaseModel):
    """ Define como uma listagem de alunos será retornada.
    """
    alunos:List[AlunoSchema]


def apresenta_alunos(alunos: List[Aluno]):
    """ Retorna uma representação do aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    result = []
    for aluno in alunos:
        result.append({
            "id": aluno.id,
            "nome": aluno.nome,
            "data_nascimento": aluno.data_nascimento,
            "sexo": aluno.sexo,
            "nome_responsavel": aluno.nome_responsavel
        })

    return {"alunos": result}


class AlunoViewSchema(BaseModel):
    """ Define como um aluno será retornado: aluno
    """
    id: int = 1
    nome: str = "Aluno da Silva"
    data_nascimento: str = "05/05/2013"
    sexo: str = "Masculino"
    nome_responsavel: str = "Responsavel da Silva"

class AlunoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    nome: str

def apresenta_aluno(aluno: Aluno):
    """ Retorna uma representação do aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    return {
        "id": aluno.id,
        "nome": aluno.nome,
        "data_nascimento": aluno.data_nascimento,
        "sexo": aluno.sexo,
        "nome_responsavel": aluno.nome_responsavel,
    }
