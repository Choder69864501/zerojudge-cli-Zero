import getpass
import zerojudge

def Initalize():
    zerojudge.user['account'] = input('Zerojudge username: ') 
    zerojudge.user['passwd'] = getpass.getpass('Account password: ')
    zerojudge.user['g-recaptcha'] = input('Recaptcha: ')
    
    zerojudge.Login()

if __name__ == '__main__':
    Initalize()
