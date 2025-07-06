import pickle
import pandas as pd

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, jsonify
from logger import logger
from flask_cors import CORS


info = Info(title="Classificador de Vinho API", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)


# Carregando o Modelo SVM treinado
with open('MachineLearning/models/svm_wine_classifier.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


# Definindo tags para a documentação da API
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
modelo_tag = Tag(name="Modelo", description="Executa o modelo de Machine Learning Classificador de Vinho")


# Rotas da API
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/classificar', tags=[modelo_tag])
def classificar():
    """Classifica um novo vinho

    Retorna a classe do vinho.
    """
    try:
        data = request.get_json(force=True)
        input_data = pd.DataFrame([data])
        classification = loaded_model.predict(input_data)
        wine_classified = int(classification[0])

        return jsonify({'prediction': wine_classified})

    except Exception as e:
        error_msg = f"Não foi possível classificar o vinho: {e}"
        logger.warning(f"Erro ao classificar vinho: {e}")
        return {"message": error_msg}, 400
