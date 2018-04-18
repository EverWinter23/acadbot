'''
18th april 2018 Wednesday
'''
from lib.webkiosk import WebKiosk
from cmds.helper import Helper
from tabulate import tabulate
from pathlib import Path
import os

webkiosk = WebKiosk()
CONFIG_FILE = 'config.txt'

def display_sgpa(cgsg):
    l = []
    for i in range(len(cgsg)):
        l.append([str(i+1), cgsg[i]['sgpa']])
    print(tabulate(l, headers=['Semester', 'SGPA']))

def cmd_sgpa():
    file = Path(CONFIG_FILE)
    if not file.exists():
        print('acadbot: Config file does not exist...')
        print('acadbot: Please run the following command first...')
        Helper().help_username()
        print('acadbot: Exiting...')
        exit()
    else:
        with open(file, 'r') as config_file:
            username = config_file.readline()
            user = username.strip('username:')
            password = config_file.readline()
            pwd = password.strip('password:')
            if user is not None and pwd is not None:
                args = {}
                args['uid'] = user
                args['pwd'] = pwd
                cgsg = webkiosk.cgpa_sgpa(args)
                display_sgpa(cgsg)
            elif user is None:
                os.remove(file)
                print('acadbot: Config file does not contain username...')
                print('acadbot: Please run the following command...')
                Helper().help_username()
                print('acadbot: Exiting...')
                exit()
