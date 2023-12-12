import requests

API_KEY='fca_live_xitMya1iF4A8tuaLH1CBVrCiEE8na3EIlFVVDhRZ'
BASIC_URL=f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES =["AUD","CAD","USD","EUR","CNY"]

def convert_currrency(base):
    currencies=",".join(CURRENCIES)
    url =f"{BASIC_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None

base = input("Please enter a currency : ").upper()

data = convert_currrency(base)
del data[base]
for ticker,value in data.items():
    print(f"{ticker} : {value} ")