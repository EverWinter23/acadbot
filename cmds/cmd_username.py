'''
16th april 2018 monday
'''
from pathlib import Path
CONFIG_FILE = 'config.txt'

def cmd_username(name):
    file = Path(CONFIG_FILE)
    if file.exists():
        with open(file, 'r') as config_file:
            line = config_file.readline()
            print('acadbot: Config file already exists for user', line.strip('username:'))

        print('acadbot: Do you want to overwrite the existing config?')
        response = input('acadbot: [yes/no]> ')
        if response == 'no':
            print("acadbot: Leaving config file as is...")
            exit()
            
        print('acadbot: Existing config will be overwritten...')
    print('acadbot: Writing to config file...')

    with open(file, 'w') as config_file:
        config_file.write(name + "\n")
    print('acadbot: Done...')




    
