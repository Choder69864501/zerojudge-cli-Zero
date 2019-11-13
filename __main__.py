from cmd import Cmd
import zerojudge

class commands(Cmd):
    intro = 'Welcome to zerojudge-cli. Type help or ? to list commands.\n'
    prompt = '>>> '

    def do_login(self, arg):
        zerojudge.Login()

    def do_submit(self, arg):
        pass

if __name__ == '__main__':
    commands().cmdloop()
