import requests
import json

formato = "json"
cep = "24315375"

url = f"https://cep.awesomeapi.com.br/{formato}/{cep}"

try:
    # Adiciona 10 de tempo para a requisição
    response = requests.get(url, timeout=10)

    # Verifica se a requisição foi bem-sucedida
    response.raise_for_status()

    # Coverte para JSON
    dados = response.json()

    # Exemplo de como acessar os dados do CEP
    print("Dados do CEP: ", dados)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # Erro HTTP
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")  # Erro de conexão
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")  # Tempo de requisição excedido
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")  # Outros erros de requisição