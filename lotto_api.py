import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'

res = requests.get(url)

#json을 python dictionary로 파싱
data = res.json()

winner = []

# js의 push와 거의 동읠
winner.append(data['drwtNo1'])
winner.append(data['drwtNo2'])
winner.append(data['drwtNo3'])
winner.append(data['drwtNo4'])
winner.append(data['drwtNo5'])
winner.append(data['drwtNo6'])