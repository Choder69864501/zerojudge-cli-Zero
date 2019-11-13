from bs4 import BeautifulSoup as bs
import requests


loginUrl = 'https://zerojudge.tw/Login'

user = {}

user['account'] = input('Please input your username: ')
user['passwd'] = input('Please input your password: ')
user['g-recaptcha'] = input('Recaptcha')


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

session = requests.Session()
session.post(loginUrl, headers=headers, data=user)

session.post('https://zerojudge.tw/Solution.api',headers=headers,data=data)

    

