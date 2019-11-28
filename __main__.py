import cmd
import getpass
import zerojudge

class commands(cmd.Cmd):
    intro = 'Welcome to zerojudge-cli. Type help or ? to list commands.\n'
    prompt = '>>> '

    def do_login(self, arg):
        'Log in to Zerojudge'
        if zerojudge.isLogged():
            print('You are already logged!!')
            return
        username = input('Please input your username: ')
        password = getpass.getpass('Please input your password: ')

        print("""
Open "https://zerojudge.tw/Login" in a private/incognito window in your browser, wait till the page loads (do not login!),
then tick "I'm not a robot" reCAPTCHA checkbox, you sometimes may need to answer some questions.
After the green checkmark appear, open the developer tools (use F12 in Firefox/Chrome),
select the console tab, and paste this line of code there and then press Enter there in the browser.  

    grecaptcha.getResponse()

A sequence of text should show up below what you pasted just now. Copy the response (the line below "Captcha response:")
and paste it here.
        """)
        recaptchaResponse = input('Please input the recaptcha response, you can use Shift+Insert to paste: ').strip('"')

        zerojudge.Login(username, password, recaptchaResponse)

    def do_submit(self, arg):
        'Submit code to specific problem: submit <problemid> <filepath> [language] (default language is c++)'
        if not zerojudge.isLogged():
            print('Please login first!')
            return

        arg = parse(arg)
        if len(arg) < 2:
            print('Too few arguments!') 
            print('Usage: submit <problemid> <filepath> [language] (default language is c++)')
        elif len(arg) > 3:
            print('Too many arguments!') 
            print('Usage: submit <problemid> <filepath> [language] (default language is c++)')
        else:
            zerojudge.Submit(*arg)

    def do_view(self, arg):
        'View specific problem: view <problemid>'

        arg = parse(arg) 
        if len(arg) < 1 or arg[0] == '':
            print('Too few arguments!') 
            print('Usage: view <problemid>')
        elif len(arg) > 2:
            print('Too many arguments!') 
            print('Usage: view <problemid>')
        else:
            zerojudge.View(*arg)

    def do_dashboard(self, arg):
        'View submissions: dashboard'   
        zerojudge.Dashboard()


    def do_exit(self, arg):
        return True


def parse(arg):
    return tuple(arg.split(' '))

if __name__ == '__main__':
    commands().cmdloop()
