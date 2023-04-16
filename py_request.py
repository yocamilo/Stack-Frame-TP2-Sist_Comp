import requests
import subprocess

# URL de la API de CoinGecko
url =   'https://api.coingecko.com/api/v3'

# URL de la API de Open Exchange Rates y ACCESKEY
url_coin    =   'https://openexchangerates.org/api/latest.json'
app_id      =   'e8c9fa33a5854cd687b823e1f2d927df'

# Flags para salir del while una vez seleccionadas las opciones validas
loop_cripto =   0
loop_coin   =   0

# while para seleccionar que criptomoneda consultar
while loop_cripto   ==  0:
    print("Seleccione la criptomoneda a consultar:")
    print("1-Bitcoin")
    print("2-Ethereum")
    cripto  =   input()
    
    if(int(cripto)  ==  1):
        print("Se ha seleccionado Bitcoin")
        currency_cripto =   'bitcoin'
        loop_cripto     =   1
    elif(int(cripto)    ==  2):
        print("Se ha seleccionado Ethereum")
        currency_cripto =   'ethereum'
        loop_cripto     =   1
    else:
        print("Seleccione una de las opciones validas")

# while para seleccionar a que moneda hacer la conversion
while loop_coin ==  0:
    print("Seleccione la moneda a convertir:")
    print("1-ARS")
    print("2-USD")
    print("3-EUR")
    currency_input  =   input()
    
    if(int(currency_input)  ==  1):
        print("Se ha seleccionado ARS")
        currency_coin   =   'ARS'
        loop_coin       =   1
    elif(int(currency_input)    ==  2):
        print("Se ha seleccionado USD")
        currency_coin   =   'USD'
        loop_coin       =   1
    elif(int(currency_input)    ==  3):
        print("Se ha seleccionado EUR")
        currency_coin   =   'EUR'
        loop_coin       =   1
    else:
        print("Seleccione una de las opciones validas")

# Solicitud GET para obtener el valor actual del BTC o ETH en dolares estadounidenses
response    =   requests.get(url + '/simple/price', params={'ids': currency_cripto, 'vs_currencies': 'usd'})

# Solicitud GET para obtener el valor de cambio del USD a ARS y EUR
response_coin   =   requests.get(url_coin, params={'app_id': app_id, 'symbols': f'USD,{currency_coin}'})

# Verificamos si las peticiones fueron exitosas
if response.status_code ==  200 and response_coin.status_code   ==  200:
    data    =   response_coin.json()

    # Definimos variable de tipo flotante donde se guarda el valor de la criptomoenda seleccionada en USD
    cripto_value    =   response.json()[currency_cripto]['usd']

    # Obtenemos el valor de USD al cambio seleccionado
    usd_to_change   =   data['rates'][currency_coin]

    cripto_value_str = str(cripto_value)
    usd_to_change_str = str(usd_to_change)

    print(cripto_value)
    print(usd_to_change)
    print("Ejecutando mylib")
    subprocess.call(['./mylib',cripto_value_str,usd_to_change_str])
    print("------------------")

else:
    print('Hubo un error en las peticiones a las APIs')





