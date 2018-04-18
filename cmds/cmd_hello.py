'''
19th april thursday 2018
'''
from pathlib import Path
from cmds.helper import Helper
from tabulate import tabulate

CONFIG_FILE = 'config.txt'
helper = Helper()

def cmd_hello():
    file = Path(CONFIG_FILE)
    if not file.exists():
        print('acadbot: Hello user. It appears you have not configured acadbot yet..')
        print('acadbot: Please run the following commands first...')
        helper.help_config()
        print('acadbot: Exiting...')
        exit()
    else:
        with open(file, 'r') as config_file:
            username = config_file.readline().rstrip('\n')
        print('acadbot: Hello ' + username + '!')
        print('acadbot: I am happy to help you with your WebKiosk needs...')
        print('')
        helper.help_helper()
        print('')
        exit()