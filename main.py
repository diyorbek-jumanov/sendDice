import requests
import os
from pprint import pprint

# token = os.environ['token']
token = '1646026624:AAFl-4-09PT5AM5T1RewNdGSo52jnLMLNv4'

def sendDice():
    url = f'https://api.telegram.org/bot{token}/sendDice'
    payload = {
        'chat_id': '1258594598',
        'emoji': '🎲'
    }
    res = requests.get(url=url, params=payload)
    



sendDice()