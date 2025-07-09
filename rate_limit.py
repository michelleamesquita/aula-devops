from flask import Flask, request, jsonify
import time

app = Flask(__name__)

rate_limit_data = {}
MAX_REQUESTS = 5
WINDOW_SECONDS = 10

def is_rate_limited(ip):
    now = time.time()
    window_start = now - WINDOW_SECONDS
    timestamps = rate_limit_data.get(ip, [])
    # Remove timestamps fora da janela
    timestamps = [ts for ts in timestamps if ts > window_start]
    if len(timestamps) >= MAX_REQUESTS:
        return True
    # Adiciona o timestamp atual
    timestamps.append(now)
    rate_limit_data[ip] = timestamps
    return False

@app.route('/')
def index():
    ip = request.remote_addr
    if is_rate_limited(ip):
        return jsonify({'erro': 'Rate limit excedido. Tente novamente mais tarde.'}), 429
    return jsonify({'mensagem': 'Requisicao aceita!'})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
