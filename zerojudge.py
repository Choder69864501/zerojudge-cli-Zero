from bs4 import BeautifulSoup as bs
import webbrowser

import requestClient 


user = None
Logged = False


def Login(username, password, recaptchaResponse):
    global user
    global Logged

    user = {
        'account': username,
        'passwd': password,
        'g-recaptcha-response': recaptchaResponse,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    loginUrl = 'https://zerojudge.tw/Login'
    requestClient.Initialize()
    if requestClient.post(loginUrl, user, headers):
        print('Login success!')
        Logged = True

def Submit(problem, path, lang='CPP'):
    path = path.strip('"')
    lang = lang.upper()
    if lang == 'C++':  # special case
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

def View(problem):
    problemUrl = 'https://zerojudge.tw/ShowProblem?problemid=' + problem
    webbrowser.open(problemUrl)

def readFile(path):
    contents = None 
    try:
        contents = open(path, "r").read()
    except (OSError, IOError) as e:
        print('File not found!')
    return contents

def isLogged():
    global Logged
    return Logged

