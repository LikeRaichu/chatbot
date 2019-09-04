import requests
from decouple import config

chat_id = ''
text = '뉴욕헤럴드트리뷴!!'
base_url = 'https://api.telegram.org'
token = config('TOKEN')

urlUpdate = f'{base_url}/bot{token}/getUpdates'

print(urlUpdate)

res = requests.get(urlUpdate)

data = res.json()

for i in range(len(data)):
    idvalue = data['result'][i]['message']['from']['id']
    realtext = (i+1)
    requests.get(f'{base_url}/bot{token}/sendMessage?chat_id={idvalue}&text={(i+1)*text}')

senders = []

for result in data['result']:
    senders.append(result['message']['chat']['id'])