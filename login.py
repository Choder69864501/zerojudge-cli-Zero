from bs4 import BeautifulSoup as bs
import requests


loginUrl = 'https://zerojudge.tw/Login'

user = {}

user['account'] = input('Please input your username: ')
user['passwd'] = input('Please input your password: ')
user['g-recaptcha'] = input('Recaptcha')


headers = {
    'Content-Type':'application/x-www-form-urlencoded',
}

session = requests.Session()
session.post(loginUrl, headers=headers, data=user)
#res = session.get('https://zerojudge.tw/Submissions?account=Cycatz')

data={'action':'SubmitCode','language':'CPP','code':'vasv','contestid':'0','problemid':'a001'}
session.post('https://zerojudge.tw/Solution.api',headers=headers,data=data)
# soup = bs(res.text, 'html.parser')
# panel = soup.select('.panel')

    

