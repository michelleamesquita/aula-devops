import requests

def buscar_usuario_github(usuario):

    url = f"https://api.github.com/users/{usuario}"

    resposta = requests.get(url)

    if resposta.status_code == 200:

        dados = resposta.json()

        print(f"Nome: {dados.get('name')}")

        print(f"Bio: {dados.get('bio')}")

        print(f"Repositórios públicos: {dados.get('public_repos')}")

        print(f"Seguidores: {dados.get('followers')}")

        print(f"Seguindo: {dados.get('following')}")

    else:

        print(f"Usuário {usuario} não encontrado.")

  

if __name__ == "__main__":

    usuario = "michelleamesquita" 

    buscar_usuario_github(usuario)