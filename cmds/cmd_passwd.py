'''
16th april 2018 monday
time 3:42am
'''
from pathlib import Path
from getpass import getpass
from cmds.helper import Helper
CONFIG_FILE = 'config.txt'

def cmd_passwd():
    file = Path(CONFIG_FILE)
    if not file.exists():
        print('acadbot: Config file does not exist...')
        print('acadbot: Please run the following command first...')
        Helper().help_username()
        print('acadbot: Exiting...')
        exit()
    print('acadbot: Found the config file...')
    with open(file, 'r') as config_file:
        line = config_file.readline()
        print('acadbot: Setting password for user', line.strip('username:'))
    with open(file, 'w') as config_file:
        config_file.write(line)  
    with open(file, 'a') as config_file:
        passwd = getpass('acadbot: [enter password]> ')
        print('')
        config_file.write("password:" + passwd)

    print('acadbot: Configuration complete...')




    
