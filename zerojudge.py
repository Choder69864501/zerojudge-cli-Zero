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
        username = input('Please input your username: ') or 'tobtob' 
        password = getpass.getpass('Please input your password: ') or 'botbot'
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

def Submit(problem, path, lang='CPP'):
    if not isLogged():
        return

    lang = lang.upper()
    if lang is 'C++':  # special case
        lang = 'CPP'
   
    if lang not in ['C', 'CPP', 'JAVA', 'PASCAL', 'PYTHON']:
        print('Your language is not supported, please choose another language!!') 
    if lang in ['C', 'CPP', 'JAVA', 'PASCAL', 'PYTHON']:
        contents = readFile(path)
        if contents:
            submitUrl = 'https://zerojudge.tw/Solution.api'
            data = {
                'action': 'SubmitCode',
                'language': lang,
                'code': contents,
                'contestid': 0,
                'problemid': problem,
            }
            if requestClient.post(submitUrl, data):
                print('Submit success!')


def readFile(path):
    contents = None 
    try:
        contents = open(path, "r").read()
    except (OSError, IOError) as e:
        print('File not found!')
    return contents

def isLogged():
    global user
    if user is None:
        print('Please login first!')
        return False
    return True



