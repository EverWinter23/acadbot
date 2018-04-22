'''
16th april 2018 monday
'''
import os
from pathlib import Path

CONFIG_FILE = 'config.txt'
HOME = str(Path.home())
DIR_PATH = HOME + "/" + '.local/share/acadbot'
FILE_PATH = DIR_PATH + "/" + CONFIG_FILE

def cmd_username(name):
    file = Path(FILE_PATH)
    if file.exists():
        with open(file, 'r') as config_file:
            line = config_file.readline()
            print('acadbot: Config file already exists for user', line)

        print('acadbot: Do you want to overwrite the existing config?')
        response = input('acadbot: [yes/no]> ')
        if response == 'no':
            print("acadbot: Leaving config file as is...")
            exit()
            
        print('acadbot: Existing config will be overwritten...')
    print('acadbot: Writing to config file...')

    dir = Path(DIR_PATH)
    if not dir.exists():        
        print('acadbot: Creating acadbot directory...')
        os.makedirs(DIR_PATH)
    
    with open(file, 'w') as config_file:
        config_file.write(name + "\n")
    print('acadbot: Done...')




    
