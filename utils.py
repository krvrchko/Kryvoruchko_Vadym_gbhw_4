import requests
from decimal import *

api = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency1 = 'eur'
currency2 = 'usd'

def currency_rates(val):
    val = val.upper()
    response = requests.get(api).text
    if val not in response:
        return None
    rur = response[(response.find('<Value>', response.find(val)) + 7)
                   :response.find('</Value>', response.find(val))]
    return Decimal(rur.replace(',', '.'))


print(f"Курс {currency1} составляет: {currency_rates(currency1)}")
print(f"Курс {currency2} составляет: {currency_rates(currency2)}")