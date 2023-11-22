import requests 

def przelicz(kwota: float, waluta_z:str, walute_na:str) -> float:
    url = f"https://v6.exchangerate-api.com/v6/da67028f6fe5d7865d9513a9/latest/{waluta_z}"
    response = requests.get(url)
    lista_walut = response.json()['conversion_rates']
    wynik=kwota*lista_walut[waluta_na]
    return wynik



print(przelicz(100,'USD', 'PLN'))


