from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from  model import Base


class Aluno(Base):
    __tablename__ = 'aluno'

    id = Column("pk_aluno", Integer, primary_key=True)
    nome = Column(String(140))
    data_nascimento = Column(String(40))
    sexo = Column(String(140))
    nome_responsavel = Column(String(140))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o aluno.
    # Essa relação é implicita, não está salva na tabela 'aluno',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.

    def __init__(self, nome:str, data_nascimento:str, sexo:str, nome_responsavel:str,
                 data_insercao:Union[datetime, None] = None):
        """
        Cria um Aluno

        Arguments:
            id: id no aluno
            nome: nome do aluno.
            data_nascimento: data de nascimento do aluno
            sexo: sexo do aluno
            nome_responsavel: nome do responsavel do aluno
            data_insercao: data de quando o aluno foi inserido à base
        """
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.nome_responsavel = nome_responsavel


        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao


