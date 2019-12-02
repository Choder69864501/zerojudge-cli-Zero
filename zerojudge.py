from bs4 import BeautifulSoup
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

def Dashboard(problem=''):
    global user
    verdictColors = {
        'TLE': '\033[1;34m',
        'CE': '\033[1;33m',
        'RE': '\033[1;36m',
        'NA': '\033[1;31m',
        'WA': '\033[1;31m',
        'AC': '\033[1;92m',
        'END': '\033[0m',
    }
    

    # params = {
    #     'account': user['account'],
    #     'problemid': problem
    # }

    # print(user)
    dashboardUrl = 'https://zerojudge.tw/Submissions?account=' + user['account']

    status = requestClient.get(dashboardUrl)
    if status['success']:
        bs = BeautifulSoup(status['res'].text, 'html.parser')
        submissionsList =  bs.find('table').find_all('tr')[1:]
        
        fields = '|{:^10}|{:^20}|{:^10}|{:^8}|{:^8}|{:^20}|'.format('ID', 'User', 'Problem', 'Result', 'Lang', 'Time') 

        print('-' * len(fields)) 
        print(fields)
        print('-' * len(fields)) 

        for sub in submissionsList:
            elements = sub.find_all('td')

            solutionId = elements[0].text
            uuser = elements[1].find('a').text # prevent conflicting with global user name
            problemId = elements[2].find('a').attrs['href'].split("problemid=", 1)[1] 
            result = elements[3].find(id='statusinfo').find(id='judgement').find().text
            result = verdictColors[result] + result + verdictColors['END']
            lang = elements[4].find(class_='SolutionCode').find(class_='btn-xs').text
            time =  elements[5].text 
            # result_detail = elements[3].find(id='statusinfo').find(id='summary')

            print('|{:^10}|{:^20}|{:^10}|'.format(solutionId, uuser, problemId), end='')
            print('  ' + result + ' ' * (17 - len(result)), end='') # because colored text will not correctly be formatted, and special case for TLE.
            print('|{:^8}|{:^20}|'.format(lang, time))

        print('-' * len(fields)) 

def readFile(path):
    contents = None 
    found = True
    try:
        contents = open(path, "r").read()
    except (OSError, IOError) as e:
        print('File not found!')
        found = False 

    if found and not contents:
        print('File is empty!')

    return contents

def isLogged():
    global Logged
    return Logged

