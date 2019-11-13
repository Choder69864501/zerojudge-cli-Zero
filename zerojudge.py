from bs4 import BeautifulSoup as bs
import requests


user = {}
session = ''


def Login():

    loginUrl = 'https://zerojudge.tw/Login'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }

    session = requests.Session()
    res = session.post(loginUrl, headers=headers, data=user)
    print(res.text)


def Submission():

    submitUrl = 'https://zerojudge.tw/Solution.api'


    

