import requests

session = None
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

def Initialize():
    global session
    session = requests.Session()

def post(url, data, headers=headers):
    success = False
    try:
        global session
        res = session.post(url, headers=headers, data=data)
        res.raise_for_status()
        success = True
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}') 
    return success

def get(url):
    global session
    res = session.get(url)
    return res


