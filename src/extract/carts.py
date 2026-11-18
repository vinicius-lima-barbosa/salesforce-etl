import requests as req

API_URL = "https://dummyjson.com/carts"

def extract_carts():
    response = req.get(API_URL, timeout=30)
    response.raise_for_status()

    data = response.json()
    carts = data.get("carts")

    if not isinstance(carts, list):
        raise ValueError("Resposta inválida: 'carts' não é uma lista.")

    return carts