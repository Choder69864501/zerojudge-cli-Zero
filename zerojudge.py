import getpass
from bs4 import BeautifulSoup as bs
from cmd import Cmd

import requestClient 


user = None


def Login():

    global user

    if user is not None:
        print('You are already logged!!')
    else:
        username = input('Please input your username: ') 
        password = getpass.getpass('Please input your password: ') 
        recaptchaResponse = input('Please input the recaptcha response, you can use Shift+Insert to paste: ') 

        loginUrl = 'https://zerojudge.tw/Login'

        user = {
            'account': username,
            'passwd': password,
            'g-recaptcha-response': recaptchaResponse,
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
        requestClient.Initialize()
        if requestClient.post(loginUrl, user, headers):
            print('Login success!')

def Submit():
    submitUrl = 'https://zerojudge.tw/Solution.api'



