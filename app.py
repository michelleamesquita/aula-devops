from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # request.host retorna 'localhost:porta', então split(':')[-1] pega a porta
    porta = request.host.split(':')[-1] if ':' in request.host else '80'
    return f"App Flask rodando na porta: {porta}"

if __name__ == '__main__':
    app.run(debug=True) 