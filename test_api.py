import pytest
import json
from app import app, loaded_model
import pandas as pd

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert '/openapi' in response.headers['Location']

def test_classificar_success(client):
    # Exemplo de dados válidos para o modelo
    data = {
        'alcohol': 13.5,
        'malic_acid': 1.5,
        'ash': 2.5,
        'alcalinity_of_ash': 18.0,
        'magnesium': 100.0,
        'total_phenols': 2.8,
        'flavanoids': 3.0,
        'nonflavanoid_phenols': 0.3,
        'proanthocyanins': 1.5,
        'color_intensity': 5.0,
        'hue': 1.0,
        'od280/od315_of_diluted_wines': 3.5,
        'proline': 1000.0
    }
    response = client.post('/classificar', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    result = response.get_json()
    assert 'prediction' in result
    assert result['prediction'] in [0, 1, 2]

def test_classificar_invalid_data(client):
    # Dados incompletos
    data = {'alcohol': 13.5}
    response = client.post('/classificar', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    result = response.get_json()
    assert 'message' in result

def test_model_predict_shape():
    # Testa se o modelo retorna uma predição para um DataFrame válido
    data = {
        'alcohol': [13.5],
        'malic_acid': [1.5],
        'ash': [2.5],
        'alcalinity_of_ash': [18.0],
        'magnesium': [100.0],
        'total_phenols': [2.8],
        'flavanoids': [3.0],
        'nonflavanoid_phenols': [0.3],
        'proanthocyanins': [1.5],
        'color_intensity': [5.0],
        'hue': [1.0],
        'od280/od315_of_diluted_wines': [3.5],
        'proline': [1000.0]
    }
    df = pd.DataFrame(data)
    prediction = loaded_model.predict(df)
    assert prediction.shape == (1,)
    assert prediction[0] in [0, 1, 2]