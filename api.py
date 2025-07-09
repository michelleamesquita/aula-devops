from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Lista em memória
itens = [
    {"id": 1, "nome": "Item 1", "descricao": "Primeiro item"},
    {"id": 2, "nome": "Item 2", "descricao": "Segundo item"},
    {"id": 3, "nome": "Item 3", "descricao": "Terceiro item"}
]

# Função auxiliar para gerar próximo id
proximo_id = 4

def get_next_id():
    global proximo_id
    id_atual = proximo_id
    proximo_id += 1
    return id_atual

@app.route('/itens', methods=['GET'])
def listar_itens():
    return jsonify(itens)

@app.route('/itens', methods=['POST'])
def criar_item():
    data = request.get_json()
    data['id'] = get_next_id()
    itens.append(data)
    return jsonify(data), 201

@app.route('/itens/<int:idx>', methods=['PUT'])
def atualizar_item(idx):
    for i, item in enumerate(itens):
        if item['id'] == idx:
            data = request.get_json()
            data['id'] = idx
            itens[i] = data
            return jsonify(data)
    return jsonify({'erro': 'Item não encontrado'}), 404

@app.route('/itens/<int:idx>', methods=['DELETE'])
def deletar_item(idx):
    for i, item in enumerate(itens):
        if item['id'] == idx:
            itens.pop(i)
            return '', 204
    return jsonify({'erro': 'Item não encontrado'}), 404

# Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'  # Caminho do seu arquivo YAML
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "API Simples com Swagger"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True) 