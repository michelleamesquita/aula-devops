import os
import requests

token = os.getenv("GITHUB_TOKEN")
def buscar_usuario_github(usuario, token):
    url = f"https://api.github.com/users/{usuario}"
    headers = {
        "Authorization": f"token {token}"
    }
    resposta = requests.get(url, headers=headers)
    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"Nome: {dados.get('name') or 'Não informado'}")
        print(f"Bio: {dados.get('bio') or 'Não informado'}")
        print(f"Repositórios públicos: {dados.get('public_repos')}")
        print(f"Seguidores: {dados.get('followers')}")
        print(f"Seguindo: {dados.get('following')}")
    else:
        print(f"Usuário {usuario} não encontrado.")

if __name__ == "__main__":
    usuario = "michelleamesquita"
    # Pegue o token de uma variável de ambiente para não expor no código
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Por favor, defina a variável de ambiente GITHUB_TOKEN com seu token do GitHub.")
    else:
        buscar_usuario_github(usuario, token)