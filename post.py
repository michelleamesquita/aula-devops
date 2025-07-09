from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/dados', methods=['POST'])
def receber_dados():
    if request.is_json:
        dados = request.get_json()
        print("Recebido:", dados)
        return jsonify({"status": "sucesso", "recebido": dados}), 200
    else:
        return jsonify({"status": "erro", "mensagem": "Corpo não é JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)