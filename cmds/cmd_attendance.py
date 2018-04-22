'''
17th april 2018 tuesday
'''

from lib.webkiosk import WebKiosk
from cmds.helper import Helper
from pathlib import Path
import os
from tabulate import tabulate

webkiosk = WebKiosk()


CONFIG_FILE = 'config.txt'
HOME = str(Path.home())
DIR_PATH = HOME + "/" + '.local/share/acadbot'
FILE_PATH = DIR_PATH + "/" + CONFIG_FILE

def display_attendance(attendance):
    # removing multiple entries of same subject
    att = [dict(t) for t in set([tuple(d.items()) for d in attendance])]
    l = []
    for i in range(len(att)):
        l.append([att[i]['name'], att[i]['Total']])
    print(tabulate(l,headers = ["Subject Name", "Total"]))

def cmd_attendance():
    file = Path(FILE_PATH)
    if not file.exists():
        print('acadbot: Config file does not exist...')
        print('acadbot: Please run the following command first...')
        Helper().help_username()
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
                attendance = webkiosk.attendance(args)
                display_attendance(attendance)
            elif uid is None:
                os.remove(file)
                print('acadbot: Config file does not contain username...')
                print('acadbot: Please run the following command...')
                Helper().help_username()
                print('acadbot: Exiting...')
                exit()








