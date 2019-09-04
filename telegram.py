import requests
from decouple import config

chat_id = '758792254'
text = '깔깔 test'
base_url = 'https://api.telegram.org'
token = config('TOKEN')

print(token)

url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

print(url)

requests.get(url)


# getUpdate 요청을 통해 받아오는 응답에서 id를 뽑아내어 sendMessage를 통해 메세지 보내기
# 1. 한 사람에게만 보내기(첫번쨰로 메세지 보낸 사람)
# 2. 나에게 메세지 보낸 모든 사람에게 보내기