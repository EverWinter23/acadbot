'''
18th april 2018 Wednesday
'''
from lib.webkiosk import WebKiosk
from cmds.helper import Helper
from tabulate import tabulate
from pathlib import Path
import os

webkiosk = WebKiosk()
helper = Helper()

CONFIG_FILE = 'config.txt'
HOME = str(Path.home())
DIR_PATH = HOME + "/" + '.local/share/acadbot'
FILE_PATH = DIR_PATH + "/" + CONFIG_FILE

def display_cgpa(cgsg):
    l = []
    l.append(['CGPA:', cgsg[len(cgsg)-1]['cgpa']])
    print(tabulate(l))

def cmd_cgpa():
    file = Path(FILE_PATH)
    if not file.exists():
        print('acadbot: Config file does not exist...')
        print('acadbot: Please run the following command first...')
        helper.help_username()
        print('acadbot: Exiting...')
        exit()
    else:
        with open(file, 'r') as config_file:
            uid = config_file.readline()
            pwd = config_file.readline()
            if uid is not None and pwd is not None:
                args = {}
                args['uid'] = uid
                args['pwd'] = pwd
                cgsg = webkiosk.cgpa_sgpa(args)
                display_cgpa(cgsg)
            elif uid is None:
                os.remove(file)
                print('acadbot: Config file does not contain username...')
                print('acadbot: Please run the following command...')
                helper.help_username()
                print('acadbot: Exiting...')
                exit()
