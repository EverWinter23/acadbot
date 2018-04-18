from pathlib import Path
from cmds.helper import Helper

CONFIG_FILE = 'config.txt'

def cmd_hello():
    file = Path(CONFIG_FILE)
    if not file.exists():
        print('acadbot: Hello user. It appears you have not configured acadbot yet..')
        print('acadbot: Please run the following commands first...')
        Helper().help_config()
        print('acadbot: Exiting...')
        exit()
    else:
        with open(file, 'r') as config_file:
            username = config_file.readline().rstrip('\n')
            user = username.strip('username:')
        print('acadbot: Hello ' + str(user) + '. Acadbot is happy to help you with your WebKiosk needs...')
        print('')
        exit()